import logging
import sys
import pandas as pd

from backend.Election import Election
from backend.ElectionRace import ElectionRace


class Runner():
    def __init__(self, configuration_file:str, candidate_file: str, ballot_file: str, result_file: str):
        self._configuration_file = configuration_file
        self._candidate_file = candidate_file
        self._ballot_file = ballot_file
        self._result_file = result_file
        self._logger = logging.getLogger("ui")

    def run(self):
        try:
            election = Election(self._configuration_file)
        except (ValueError, KeyError, IOError):
            self._logger.error("Unable to parse configuration file from `%s`.", self._configuration_file,
                              exc_info=sys.exc_info())
            sys.stderr.write("Unable to load configuration file. Please verify that the file specified is the correct configuration file.")
            return

        try:
            election.load_candidates(self._candidate_file)
        except (ValueError, KeyError, IOError):
            self._logger.error("Unable to load candidate file from `%s`.", self._candidate_file, exc_info=sys.exc_info())
            sys.stderr.write("Unable to load candidate file. Please verify that the file specified is the correct candidate file.")
            return

        try:
            election.load_ballots(self._ballot_file)
        except (ValueError, KeyError, IOError):
            self._logger.error("Unable to load ballot file from `%s`.", self._ballot_file, exc_info=sys.exc_info())
            sys.stderr.write("Unable to load ballot file. Please verify that the file specified is the correct ballot file.")
            return

        with pd.ExcelWriter(self._result_file) as writer:
            for race in election.get_race_all():
                race.run_complete()
                result_table = ElectionRace.get_data_table(race.get_round_latest())
                df = pd.DataFrame(result_table, columns=["Candidate", "Party", "Status", "Score", "QuotaPercentage"])
                df.drop(columns=["QuotaPercentage"], inplace=True)
                df.to_excel(writer, sheet_name=race.position())

        pass
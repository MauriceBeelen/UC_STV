from backend.ElectionQuota import ElectionQuota


class HareQuota(ElectionQuota):
    def __init__(self, voters:int, max_winners: int):
        self._voters = voters
        self._max_winners = max_winners

    def get_quota(self) -> int:
        """Return the hare quota for the election race.

        This value returned will always be an integer value and is calculated
        based upon the number of voters and the maximum number of winners.

        - If the number of winners is just one, then the hare quota is calculated
        as: (# of voters)/(max. # of winners).
        """
        return_value = int(self._voters / self._max_winners)

        return return_value if return_value > 0 else 1


class DroopQuota(ElectionQuota):
    def __init__(self, voters: int, max_winners: int):
        self._voters = voters
        self._max_winners = max_winners

    def get_quota(self) -> int:
        """Return the droop quota for the election race.

        This value returned will always be an integer value and is calculated
        based upon the number of voters and the maximum number of winners.

        - If the number of winners is greater than one, then the droop quota is
        calculated as: (# of voters)/(max. # of winners + 1) + 1.
        - If the number of winners is just one, then the droop quota is calculated
        as: (# of voters + 1)/2.
        """
        return_value = 0
        if self._max_winners > 1:
            return_value = int((self._voters / (self._max_winners + 1)) + 1)
        elif self._max_winners == 1:
            return_value = int((self._voters + 1) / 2)

        return return_value if return_value > 0 else 1
import logging

from interfaces.cmd.Runner import Runner


def run(parsed_arguments):
    log_destination = parsed_arguments.log_destination
    log_level = parsed_arguments.log_level

    # Setup logging in the application.
    logger = logging.getLogger("cmd")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(process)d: %(asctime)s - %(name)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler(filename=log_destination + "/cmd.log", encoding="utf-8")
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    if not parsed_arguments.config_file:
        raise ValueError("Missing configuration file argument")
    if not parsed_arguments.candidate_file:
        raise ValueError("Missing candidate file argument")
    if not parsed_arguments.ballot_file:
        raise ValueError("Missing ballot file argument")
    if not parsed_arguments.result_file:
        raise ValueError("Missing result file argument")

    runner = Runner(parsed_arguments.config_file,
                    parsed_arguments.candidate_file,
                    parsed_arguments.ballot_file,
                    parsed_arguments.result_file)

    runner.run()




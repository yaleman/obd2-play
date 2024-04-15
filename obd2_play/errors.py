import click

import obd  # type: ignore
from loguru import logger

from obd2_play import startup


@click.command()
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging")
def main(debug: bool) -> None:
    connection = startup(debug)
    if connection is None:
        logger.error("Couldn't connect")
        return

    logger.info("Querying Error Codes")
    response = connection.query(obd.commands.GET_DTC)
    # https://github.com/brendan-w/python-OBD/wiki/Command-Tables#mode-03
    if response.value is None:
        logger.error("No errors returned")
    else:
        logger.info("Dumping errors")
        for code in response.value:
            logger.info(code)

    """
    example output:
    [
    ("P0030", "HO2S Heater Control Circuit"),
    ("P1367", "Unknown error code")
    ]
    """

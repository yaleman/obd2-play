from time import sleep
import click
import obd  # type: ignore
import obd.commands  # type: ignore
from loguru import logger

from obd2_play import startup


@click.command()
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging")
def main(debug: bool) -> None:
    connection = startup(debug)
    while True:
        logger.info("RPM: {}", connection.query(obd.commands.RPM))
        logger.info("FUEL_STATUS: {}", connection.query(obd.commands.FUEL_STATUS))
        sleep(1)

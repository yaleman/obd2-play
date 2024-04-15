from time import sleep
import click
import obd  # type: ignore
import obd.commands  # type: ignore
from loguru import logger

from obd2_play import startup


@click.command()
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging")
@click.option(
    "-s", "--show-commands", is_flag=True, help="Show available commands and quit"
)
def main(debug: bool, show_commands: bool) -> None:
    connection = startup(debug)
    if connection is None:
        logger.error("Couldn't connect")
        return
    available_commands = connection.supported_commands
    if show_commands:
        for command in available_commands:
            print(command)
        return

    wanted_commands = {
        "RPM": "RPM",
        "FUEL_STATUS": "FUEL_STATUS",
        "VOLTAGE": "CONTROL_MODULE_VOLTAGE",
        "ELM_VOLTAGE": "ELM_VOLTAGE",
    }

    while True:

        for key, value in wanted_commands.items():
            if key in available_commands:
                logger.info(f"{key}: {connection.query(getattr(obd.commands, value))}")

        sleep(1)

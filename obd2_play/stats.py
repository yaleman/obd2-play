import sys

import obd  # type: ignore
import obd.commands  # type: ignore
from loguru import logger


def main() -> None:
    logger.info("Starting connection")
    connection = obd.OBD()
    if not connection.is_connected():
        logger.error("Not connected!")
        sys.exit(1)
    else:
        logger.info("Using port {}", connection.port_name())

    while True:
        logger.info("RPM: {}", connection.query(obd.commands.RPM))
        logger.info("FUEL_STATUS: {}", connection.query(obd.commands.FUEL_STATUS))

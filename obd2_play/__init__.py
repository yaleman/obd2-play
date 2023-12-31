import sys
import obd
from loguru import logger


def startup(debug: bool = False) -> obd.OBD:
    """do startup things"""
    if debug:
        obd.logger.setLevel(obd.logging.DEBUG)
    ports = obd.scan_serial()
    ports = [port for port in ports if "usbserial" in port]

    for port in ports:
        logger.info("Starting connection on {}", port)
        connection = obd.OBD(portstr=port)

        logger.debug(
            "Using interface '{}' port '{}' status: {}",
            connection.interface,
            connection.port_name(),
            connection.status(),
        )
        if not connection.is_connected():
            logger.error("Not connected!")
            continue
        return connection
    logger.error("Couldn't find port!")
    sys.exit(1)

import sys

import obd  # type: ignore
from loguru import logger

logger.info("Starting connection")
connection = obd.OBD()
if not connection.is_connected():
    logger.error("Not connected!")
    sys.exit(1)
else:
    logger.info("Using port {}", connection.port_name())


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

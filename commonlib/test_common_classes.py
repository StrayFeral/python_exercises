#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple test for some of the functions in common_classes.py

Not a proper unit testing, but still - a good test."""

import logging
import time

from common_classes import GenericClass
from common_classes import SignalHandlers
from common_classes import UserInterfaceBasics
from common_classes import MathTools
from common_classes import BasicCountryInfo


# Default logging config
logging_format = "[%(asctime)s][%(levelname)-8s][%(funcName)s] %(message)s"
logging_level = logging.DEBUG

logging.basicConfig(level=logging_level, format=logging_format)
logger = logging.getLogger(__name__)


logger.info("TESTING some functions from common.py ...\n")


logger.info("---")

# Negative test: This works and raises exception about country not found
# logger.info("Testing BasicCountryInfo, getting a hotfixed country: {0}".format(BasicCountryInfo.get("@@@")))
logger.info(
    "Testing BasicCountryInfo, getting a hotfixed country: {0}".format(
        BasicCountryInfo.get("@@")
    )
)
logger.info(
    "Testing BasicCountryInfo, getting a Bulgaria: {0}".format(
        BasicCountryInfo.get("bgr")
    )
)

logger.info("---")


class Specific(GenericClass):
    def hey(self):
        self.logger.info("A message from a SpecificObject")


specific_obj = Specific()
specific_obj.hey()

logger.info("---")

SignalHandlers.set_ctrl_c_handler()
logger.debug(
    "CTRL-C handler is now set. Now looping for test of SIGINT ... press CTRL+C ..."
)
try:
    while True:
        pass
except KeyboardInterrupt:
    logger.debug("exiting ...")

logger.info("---")

UserInterfaceBasics.make_shell_pause()

logger.info("---")

progress_args = {"total": 10, "value": 1}
progress_args = MathTools.calculate_percentage(progress_args)
progress_args = MathTools.calculate_eta(progress_args)
logger.debug("calculate_percentage() 1/10: {0}%".format(progress_args["percentage"]))
logger.debug("calculate_eta(): {0}".format(progress_args["eta"]))

logger.info("---")

logger.debug("Sleeping 5 seconds ...")
time.sleep(5)

progress_args["value"] = 5
progress_args = MathTools.calculate_percentage(progress_args)
progress_args = MathTools.calculate_eta(progress_args)
logger.debug("calculate_percentage() 5/10: {0}%".format(progress_args["percentage"]))
logger.debug("calculate_eta(): {0}".format(progress_args["eta"]))

logger.info("---")

logger.debug("Sleeping 5 seconds ...")
time.sleep(5)

progress_args["value"] = 10
progress_args = MathTools.calculate_percentage(progress_args)
progress_args = MathTools.calculate_eta(progress_args)
logger.debug("calculate_percentage() 10/10: {0}%".format(progress_args["percentage"]))
logger.debug("calculate_eta(): {0}".format(progress_args["eta"]))

logger.info("---")

logger.info("Done.")

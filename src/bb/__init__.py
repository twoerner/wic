"""
Minimal stub of BitBake's bb module for standalone wic.
Provides debug logging used by vendored oe helpers.
"""
import logging

def debug(level, msg):
    """
    Mirror bb.debug signature but route to standard logging.
    """
    logging.getLogger("bb").debug(msg)

# The utils submodule is provided in bb.utils

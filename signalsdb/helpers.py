"""
    signalsdb.helpers
    ~~~~~~~~~~~~~~~~~

    Defines utility functions.
"""


import re


def compile_re(pattern):
    """
    Convert a *pattern* into a regex object compiled
    with the IGNORECASE flag.

    :param pattern: A regex (string).
    """
    return re.compile(pattern, re.IGNORECASE)

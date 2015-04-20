"""
    signalsdb.helpers
    ~~~~~~~~~~~~~~~~~

    Defines utility functions.
"""


from fnmatch import translate
import re


def compile_glob(glob):
    """
    Compile a glob into a regex object compiled
    with the IGNORECASE flag.

    :param glob: A glob (string).
    """
    return re.compile(translate(glob), re.IGNORECASE).search

from fnmatch import translate
from re import compile, IGNORECASE


def compile_glob(glob):
    return compile(translate(glob), IGNORECASE).search

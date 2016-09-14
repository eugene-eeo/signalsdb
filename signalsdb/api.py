"""
    signalsdb.api
    ~~~~~~~~~~~~~

    Exports the public API.
"""


import re
from signalsdb.db import SIGNALS

__all__ = ('explain', 'search')


class NoSuchSignal(KeyError):
    """
    The given signal wasn't found in the DB.
    """
    pass


def explain(code, signals=SIGNALS):
    """
    Explain what a given integer signal *code* does,
    including it's signal name.

    :param code: An integer signal.
    :param signals: A database of signals.
    """
    if code not in signals:
        raise NoSuchSignal(code)
    signal, action, description = signals[code]
    return {
        'id': code,
        'signal': signal,
        'action': action,
        'description': description,
        }


def search(signal='', action='', signals=SIGNALS):
    """
    Search the signals DB for signal named *signal*,
    and which action matches *action* in a case
    insensitive way.

    :param signal: Regex for signal name.
    :param action: Regex for default action.
    :param signals: Database of signals.
    """
    sig_re = re.compile(signal, re.IGNORECASE)
    act_re = re.compile(action, re.IGNORECASE)
    res = []
    for code in signals:
        sig, act, _ = signals[code]
        if sig_re.match(sig) and act_re.match(act):
            res.append(explain(code, signals=signals))
    return res

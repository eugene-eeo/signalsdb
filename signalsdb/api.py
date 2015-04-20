"""
    signalsdb.api
    ~~~~~~~~~~~~~

    Exports the public API.
"""


from signalsdb.db import SIGNALS
from signalsdb.helpers import compile_re

__all__ = ('explain', 'search')


def explain(code, signals=SIGNALS):
    """
    Explain what a given *code* does, including it's
    signal name.

    :param code: An integer signal.
    :param signals: A database of signals.
    """
    signal, action, description = signals[code]
    return dict(
        id=code,
        signal=signal,
        action=action,
        description=description,
        )


def search(signal='', action='', description='', signals=SIGNALS):
    """
    Search the signals database for a signal given
    it's *signal*, *action* and *description* queries
    in the form of regexes, in a case-insensitive way.

    :param signal: Signal query (regex).
    :param action: Action query (regex).
    :param description: Description query (regex).
    :param signals: A database of signals.
    """
    q_sig = compile_re(signal).match
    q_act = compile_re(action).match
    q_dsc = compile_re(description).match

    arr = []
    for code in signals:
        sig, act, dsc = signals[code]
        if q_sig(sig) and q_act(act) and q_dsc(dsc):
            arr.append(explain(code, signals=signals))
    return arr

"""
    signalsdb.api
    ~~~~~~~~~~~~~

    Exports the public API.
"""


from signalsdb.db import SIGNALS
from signalsdb.helpers import compile_re, NoSuchSignal

__all__ = ('explain', 'search')


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
    sig_matches = compile_re(signal).match
    act_matches = compile_re(action).match
    res = []
    for code in signals:
        sig, act, _ = signals[code]
        if sig_matches(sig) and act_matches(act):
            res.append(explain(code, signals=signals))
    return res

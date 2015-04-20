"""
    signalsdb.api
    ~~~~~~~~~~~~~

    Exports the public API.
"""


from signalsdb.db import SIGNALS
from signalsdb.helpers import compile_glob

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


def search(signal='*', action='*', description='*', signals=SIGNALS):
    """
    Search the signals database for a *signal*,
    it's default *action*, and the *description*
    in a case-insensitive way using the glob
    syntax.

    :param signal: The signal query.
    :param action: The action query.
    :param description: The description query.
    :param signals: A database of signals.
    """
    q_sig = compile_glob(signal)
    q_act = compile_glob(action)
    q_desc = compile_glob(description)

    arr = []
    for code in signals:
        sig, action, desc = signals[code]
        if q_sig(sig) and q_act(action) and q_desc(desc):
            arr.append(explain(code, signals=signals))
    return arr

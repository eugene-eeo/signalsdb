from signalsdb.db import SIGNALS
from signalsdb.helpers import compile_glob

__all__ = ('explain', 'search')


def explain(code, signals=SIGNALS):
    signal, action, description = signals[code]
    return dict(
        id=code,
        signal=signal,
        action=action,
        description=description,
        )


def search(signal='*', action='*', description='*', signals=SIGNALS):
    q_sig = compile_glob(signal)
    q_act = compile_glob(action)
    q_desc = compile_glob(description)

    arr = []
    for code in signals:
        sig, action, desc = signals[code]
        if q_sig(sig) and q_act(action) and q_desc(desc):
            arr.append(explain(code))
    return arr

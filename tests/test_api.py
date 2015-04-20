from pytest import mark
from signalsdb.api import explain, search


SIGNALS = {
    13: ('SIGNAL', 'Action', 'Desc'),
    14: ('SIGNAT', 'Kill', 'Desc'),
}


def test_explain():
    assert explain(13, signals=SIGNALS) == {
            'action': 'Action',
            'description': 'Desc',
            'id': 13,
            'signal': 'SIGNAL',
        }


@mark.parametrize('signal,action,description', [
    ('signal', '(ACTION|Kill)', '\w+'),
    ('SIGNA*', 'action', 'De[sc]{,2}'),
])
def test_search(signal, action, description):
    assert search(signal=signal,
                  action=action,
                  signals=SIGNALS) == [explain(13, signals=SIGNALS)]

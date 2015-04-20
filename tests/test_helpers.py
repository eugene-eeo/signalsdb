from signalsdb.helpers import compile_re


def test_compile_glob():
    assert compile_re('\w*').match('4ny_tExt')
    assert compile_re('TEST*').match('testa')
    assert compile_re('ignores_case').match('IGNORES_CASE')

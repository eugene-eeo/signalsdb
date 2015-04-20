from signalsdb.helpers import compile_glob


def test_compile_glob():
    assert compile_glob('*')('4ny_tExt')
    assert compile_glob('TEST*')('testa')
    assert compile_glob('ignores_case')('IGNORES_CASE')

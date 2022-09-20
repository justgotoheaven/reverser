from reverse_function import reverse_string


def test_string():
    assert reverse_string('test') == 'tset'


def test_empty():
    assert reverse_string('') == -1


def test_spaces():
    assert reverse_string('  ') == -2


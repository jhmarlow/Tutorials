"""content of test_sample.py."""


def func(x):
    """doc."""
    return x + 1


def test_answer():
    """doc."""
    assert func(3) == 4

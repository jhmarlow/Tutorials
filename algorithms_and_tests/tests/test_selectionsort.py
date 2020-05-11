"""tests."""

from selection_sort import selection_sort


def test_list():
    """test."""
    assert selection_sort([64, 25, 12, 22, 11]) == [13, 12, 22, 25, 64]


# content of test_class.py
class TestClass:
    """doc."""
    
    def test_one(self):
        """doc."""
        x = "this"
        assert "h" in x

    def test_two(self):
        """doc."""
        x = "hello"
        assert hasattr(x, "check")

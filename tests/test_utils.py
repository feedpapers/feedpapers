import feedpapers.utils as utils


def test_internet():
    assert utils.internet() is True

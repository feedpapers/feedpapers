import pandas as pd
import pytest

import importlib.util

spec = importlib.util.spec_from_file_location("feedpapers", "feedpapers/feedpapers.py")
feedpapers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(feedpapers)


def test_running():
    feedpapers.limnotoots(tweet=False, interactive=False, to_csv=True)
    d = pd.read_csv("test.csv")
    assert isinstance(d, pd.DataFrame)

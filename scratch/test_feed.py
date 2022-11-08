import os
import sys
import inspect
import feedparser as fp
import pandas as pd
import pytest

import importlib.util

spec = importlib.util.spec_from_file_location("feedpapers", "feedpapers/feedpapers.py")
feedpapers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(feedpapers)

url = "https://www.tandfonline.com/feed/rss/ulrm20"
posts = []

feed = fp.parse(url)
for post in feed.entries:
    posts.append(post)

res = pd.DataFrame(posts)
# print(res.columns)
# res = res.rename(columns = {"link": "prism_url"})
#
# res = res.drop(columns = ["summary"])
# res = res.rename(columns = {"description_encoded": "summary"})

res.filter(items=["updated"])


def test_fields():
    has_published = len(set(list(res.columns)).intersection(["title", "link"])) == 2
    has_updated = len(set(list(res.columns)).intersection(["title", "link"])) == 2
    assert has_published or has_updated


res.to_csv("test.csv")

print(res)
print(res["summary"])
res = feedpapers.filter_limno(res)["papers"]
print(res)
print(res["title"])
toots = res["title"] + ". " + res["link"]

toots.__class__
toots.sample(frac=1)

for toot in toots:
    print(toot)

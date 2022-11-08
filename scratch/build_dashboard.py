import pandas as pd
import datetime
from feedpapers import limnotoots
from numpy import nan as Nan


# get latest tweet date per dc_source
log_raw = pd.read_csv("log.csv")
log_raw["date"] = pd.to_datetime(log_raw["date"])
log = log_raw.loc[log_raw["posted"] != "i"]
labels = log.groupby("dc_source").date.idxmax()
log = log.loc[log.index.intersection(labels)]  # filter most recent tweets
log = log.reset_index(drop=True)
log["date"] = log["date"].dt.strftime("%Y-%m-%d")

# get number of tweets per dc_source
limnotoots(tweet=False, interactive=False, to_csv=True)
d = pd.read_csv("test.csv")
d["updated"] = pd.to_datetime(d["updated"])
labels = d.groupby("dc_source").updated.idxmax()
d = d.loc[d.index.intersection(labels)]
d = d.reset_index(drop=True)
d["updated"] = d["updated"].dt.strftime("%Y-%m-%d")

# create tables
# need to escape spaces in dc_source?
latest = log.assign(
    badge="![alt text](https://img.shields.io/badge/"
    + log["dc_source"].replace(regex=" ", value="%20")
    + "-"
    + log["date"].replace(regex="-", value="--")
    + "-green.svg)"
)
latest = latest[["badge", "dc_source"]]
latest = latest.rename(index=str, columns={"badge": "Last tweet"})

state = d.assign(
    badge="![alt text](https://img.shields.io/badge/"
    + d["dc_source"].replace(regex=" ", value="%20")
    + "-"
    + d["updated"].replace(regex="-", value="--")
    + "-green.svg)"
)
state = state[["badge", "dc_source"]]
state = state.rename(index=str, columns={"badge": "Last RSS entry"})

table_raw = state.set_index("dc_source").join(latest.set_index("dc_source"))
table_raw = table_raw.reset_index(drop=True)
table_raw = table_raw[["Last tweet", "Last RSS entry"]]
table_raw = table_raw.fillna("&nbsp;")

cols = table_raw.columns
blank_line = pd.Series([Nan, Nan], index=cols)
# cols = "| " + " | ".join(table_raw.columns) + " |"
header = pd.DataFrame(
    [
        [
            "---",
        ]
        * len(cols)
    ],
    columns=cols,
)
table = pd.concat([header, table_raw])
# table = table.append(blank_line, ignore_index=True)
table.to_csv("dashboard.md", sep="|", index=False)
table = open("dashboard.md", "a")
table.write("\n")
table.close()

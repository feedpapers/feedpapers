# feedpapers

![pytest](https://github.com/jsta/feedpapers/workflows/pytest/badge.svg)

Code to monitor [limnology RSS feeds](feedpapers/journals.csv) and [tweet](https://twitter.com/limno_papers) new articles.

## Scope

The keywords and journal choices herein aim to focus on limnology (the study of inland waters). They are also meant to exclude related topics such as fisheries ecology, water resources engineering, estuarine/marine ecology, ecological genetics, and the study of specific "inland seas" like the North American Great Lakes. Feel free to weigh-in in the repository issues on scope recommendations! 

## Usage

Query papers that came out prior to today without tweeting:

`feedpapers`

Query papers that came out prior to today and open in browser:

`feedpapers --browser`

Manually approve tweeting of papers that came out prior to today:

`feedpapers --interactive`

Unsupervised tweeting of papers that came out prior to today:

`feedpapers --tweet`

"Reset" the tweet log:
```shell
feedpapers --ignore_all
# manually delete old log entries
```

## Setup

### Enable tweeting (optional)

* Create a file named `config.py` that stores your twitter API keys

### Enable unsupervised tweeting (optional)

* Create a _cron_ job. On Linux this can be done with the following commands:

```
crontab -e 
0 15 * * * python /path/to/feedpapers.py
```

### Python dependencies

See [requirements.txt](requirements.txt)

Install these to the activated environment with:

`pip install -r requirements.txt`

## Contributing

* Please help by adding missing journals to [feedpapers/journals.csv](feedpapers/journals.csv) or filing an [issue](https://github.com/jsta/feedpapers/issues)

* Filtering keywords are located in [feedpapers/keywords.csv](feedpapers/keywords.csv).

## Prior art

https://github.com/ropenscilabs/data-packages

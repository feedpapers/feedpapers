# feedpapers

[![pytest](https://github.com/feedpapers/feedpapers/actions/workflows/pytest.yml/badge.svg)](https://github.com/feedpapers/feedpapers/actions/workflows/pytest.yml)

Code to monitor [journal RSS feeds](feedpapers/journals.csv) and [tweet](https://twitter.com/limno_papers) new articles.

## Scope

The scope of the feed is defined by entries in keywords.csv 

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

or

`conda env create -f environment.yml`

## Contributing

* Please help by adding missing journals to [feedpapers/journals.csv](feedpapers/journals.csv) or filing an [issue](https://github.com/jsta/feedpapers/issues)

* Filtering keywords are located in [feedpapers/keywords.csv](feedpapers/keywords.csv).

## Prior art

https://github.com/ropenscilabs/data-packages

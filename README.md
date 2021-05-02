# scorewriter

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

This project is a scorewriter developed at welcome seminar.

## Requirement

- Python 3.8
- pipenv

## Installation

```sh
$ git clone <this repo>
$ cd <this repo>
$ pipenv install
```

## Usage

### Run app

- `pipenv run start --run` - run scorewriter app
- `pipenv run start --analyzer` - display spectrum analyzer
- `pipenv run start --help` - print help

### Generate analyzer format

If you want to customize the output format of the analyzer, follow the steps below.

1. set `N_MUSICAL_SCALE` and `N_DRAWED_STATES` in `./core/config.py`
2. run `pipenv run ./generate_anal_template.py`

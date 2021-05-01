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

### Generate analyzer format

1. set `N_MUSICAL_SCALE` and `N_DRAWED_STATES` in `./core/config.py`
2. run `./generate_anal_template.py`

### Run app

```sh
$ pipenv run start
```

#!/usr/bin/env python3
import argparse

from core import analyzer
from core import detector
import spectrum_analyzer


def run_app() -> None:
    # set analyzer
    piano_analyzer = analyzer.Analyzer()

    while True:
        key_states: list = detector.get_key_states()
        piano_analyzer.update(key_states)


if __name__ == "__main__":
    # options
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('-a', '--analyzer',
                        help='display spectrum analyzer',
                        action='store_true')
    parser.add_argument('-r', '--run',
                        help='run scorewriter',
                        action='store_true')
    args = parser.parse_args()

    if args.run:
        run_app()
    if args.analyzer:
        spectrum_analyzer.run_app()

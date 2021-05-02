#!/usr/bin/env python3
import argparse
import time
import random

from core import analyzer
from core import config
import spectrum_analyzer


def run_app() -> None:
    piano_analyzer = analyzer.Analyzer()

    while True:
        key_states: list = [0 if random.random(
        ) < 0.8 else 1 for _ in range(config.N_MUSICAL_SCALE)]
        piano_analyzer.update(key_states)

        # delay
        time.sleep(0.2)


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

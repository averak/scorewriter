#!/usr/bin/env python3
import time
import random

from core import analyzer
from core import config

piano_analyzer = analyzer.Analyzer()

while True:
    key_states: list = [0 if random.random() < 0.8 else 1 for _ in range(config.N_MUSICAL_SCALE)]
    piano_analyzer.update(key_states)

    # delay
    time.sleep(0.2)

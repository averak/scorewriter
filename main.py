#!/usr/bin/env python3
import time
import random

from core import analyzer

piano_analyzer = analyzer.Analyzer()

while True:
    # key_states: list = [random.randint(0, 1) for i in range(7)]
    key_states: list = [0 if random.random() < 0.8 else 1 for i in range(7)]
    piano_analyzer.update(key_states)

    # delay
    time.sleep(0.2)

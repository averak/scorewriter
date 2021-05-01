#!/usr/bin/env python3
from core import config

dump_txt: str = ""

# generate musical scale boxes
dump_txt += " "
dump_txt += "   ".join(["###" for _ in range(config.N_MUSICAL_SCALE)])
dump_txt += "\n"

# generate key states field
for _ in range(config.N_DRAWED_STATES):
    dump_txt += "$-\n"

# dump to config file
with open(config.ANALYZER_TEMPLATE_PATH, "w") as f:
    f.write(dump_txt)

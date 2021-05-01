import anal

from . import config


class Analyzer:
    def __init__(self):
        self.analyzer = anal.Anal(config.ANALYZER_TEMPLATE_PATH)
        self.analyzer.init_draw()

        # states of each key per time-frame
        # 0: not pushed, 1: pushed
        self.key_states_list: list = [
            [0] * config.N_MUSICAL_SCALE for _ in range(config.N_DRAWED_STATES)]

    def update(self, key_states: list) -> None:
        # clear old states
        self.key_states_list.pop(-1)
        # push new states
        self.key_states_list.insert(0, key_states)

        # update analyzer!
        self.analyzer.draw(*self.create_draw_args())

    def create_draw_args(self) -> list:
        result: list = []

        for key_states in self.key_states_list:
            pushed_color: str = "\x1b[42m   \x1b[0m"
            drawed_str: str = "   ".join(map(lambda s: pushed_color if s else "   ", key_states))
            result.append(drawed_str)

        return result

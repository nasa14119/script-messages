from src.const import current_index
import json
from src.keyboard import controller
from pynput.keyboard import Key


def enter():
    controller.press(Key.enter)
    controller.release(Key.enter)


class Message:
    def parse_data():
        pass

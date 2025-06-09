from src.const import current_index, phones
import json
import pandas as pd
import platform

from pynput.keyboard import Key, Controller
from time import sleep
from PIL import Image
import pyperclipimg as pci
import pyperclip as pc
import re


values = dict()


def set_data():
    global config
    global values
    with open("config.json", "r") as file:
        config = json.load(file)
    data_csv = pd.read_csv(
        config["data"]["path"], dtype={config["data"]["phone_property"]: str}
    )
    if len(config["vars"]) == 0:
        return
    start = data_csv[data_csv[config["data"]["phone_property"]] == phones[0]].index[0]
    end = data_csv[data_csv[config["data"]["phone_property"]] == phones[-1]].index[-1]
    sliced_df = data_csv.loc[start:end]
    for _, row in sliced_df.iterrows():
        phone = row[config["data"]["phone_property"]]
        values[phone] = {}
        for value in config["vars"]:
            values[phone][value] = row[value]


def get_template():
    with open("template.json", "r") as file:
        template = json.load(file)
    return template


controller = Controller()


def enter():
    global controller
    controller.press(Key.enter)
    controller.release(Key.enter)


def paste():
    global controller
    if platform.system() == "Windows":
        with controller.pressed(Key.ctrl):
            controller.press("v")
            controller.release("v")
    else:
        with controller.pressed(Key.cmd):
            controller.press("v")
            controller.release("v")


class Message:
    def __init__(self):
        set_data()
        self.message_list = list()
        self.parse_data()

    def __set_image(self, path):
        try:
            img = Image.open(path)
            return lambda: pci.copy(img)
        except:
            raise RuntimeError("Something wrong with current img")

    def __set_text_var(self, str):
        global values
        matches = re.findall(r"\[([^\[\]]+)\]", str)
        for match in matches:
            str = str.replace(f"[{match}]", f"{{{match}}}")
        func_srt = lambda phone: str.format(**values[phone])
        return lambda phone: pc.copy(func_srt(phone))

    def parse_data(self):
        global values
        global current_index
        template = get_template()
        opt = {
            "img": lambda body: self.__set_image(body),
            "text_var": lambda body: self.__set_text_var(body),
            "text": lambda body: lambda: pc.copy(body),
        }
        for comp in template:
            self.message_list.append(
                {
                    "type": comp["type"],
                    "body": opt[comp["type"]](comp["body"]),
                }
            )

    def send(self):
        global current_index
        for message in self.message_list:
            enter()
            if message["type"] == "img":
                message["body"]()
                paste()
            elif message["type"] == "text_var":
                message["body"](current_index.phone)
                paste()
            else:
                message["body"]()
                paste()
            enter()
            sleep(1)
            pc.copy("")
        enter()


messages = Message()

import pandas as pd
import json


def get_phones():
    with open("config.json", "r") as file:
        config = json.load(file)
    config = config["data"]
    phones_column = pd.read_csv(config["path"], dtype={config["phone_property"]: str})
    phones_list = list(phones_column[config["phone_property"]])
    start = (
        0 if not hasattr(config, "start") and not config["start"] else config["start"]
    )
    end = -1 if not hasattr(config, "end") and not config["end"] else config["end"]
    return phones_list[start - 2 : end - 1]

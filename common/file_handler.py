import os
from typing import List
import pickle
from task1 import config
from common.models import StoreItem
from common.zip_code_handler import get_position_for_zip_code


def parse_line(line: str) -> (str, str):
    # dirty hack how to get rid of "
    raw_key, raw_val = line.split(":")
    return raw_key.strip()[1:-1], raw_val.strip()[:-1].replace("\"", "")


def process_file_content(path: str) -> List[StoreItem]:
    # this part is for quicker testing so we don't have to wait till data from API are fetched
    if _does_file_exist(config.OUT_PATH):
        with open(config.OUT_PATH, "rb") as f:
            return pickle.load(f)
    # -------------------------------------------------------

    # Not a pythonic way here but the cycle is quite complex
    data = []
    item = StoreItem()
    with open(path, "r") as f:
        # Could be replaced by json.load() - I was trying to avoid libs as README advises
        for line in f:
            if _should_skip(line):
                if not item.is_empty():
                    item.location = get_position_for_zip_code(item.postcode)
                    if item.location:
                        # do not show the stores without GPS location
                        data.append(item)
                item = StoreItem()
                continue

            key, val = parse_line(line)
            item.__setattr__(key, val)
        data.sort()
        save_results(data)
        return data


def _should_skip(line: str) -> bool:
    return "name" not in line and "postcode" not in line


def _does_file_exist(file_path: str) -> bool:
    return os.path.isfile(file_path)


def save_results(data: List[StoreItem]):
    # helper function for caching - just not to fetch postcodes on every start
    if not _does_file_exist(config.OUT_PATH):
        with open(config.OUT_PATH, "wb") as f:
            pickle.dump(data, f)
from dataclasses import asdict
from typing import List

from common.file_handler import process_file_content
from common.models import StoreItem
from task2 import config


def filter_store(substring: str) -> List[StoreItem]:
    data = process_file_content(config.DATA_PATH)
    # if no substring, return all
    if not substring:
        return data

    # case insensitive
    filtered_postcode = list(filter(lambda x: substring in x.postcode.lower(), data))
    filtered_name = list(filter(lambda x: substring in x.name.lower(), data))
    final_result = filtered_postcode + filtered_name
    return final_result

from typing import List

import requests
from common.models import StoreItem

from task1 import config

# Deprecated approach with API and limitation for 2000 meters


def _generate_hash_table(data: List[StoreItem]) -> dict:
    # performance improvement
    return {item.postcode: item for item in data}


def find_close_postcodes(postcode: str, radius: int):
    raw_response = requests.get(
        f"{config.API_BASE_URL}/postcodes/{postcode}/nearest", params={"radius": radius}
    )
    if raw_response.status_code == 200:
        json_response = raw_response.json()
        # results include the searched post code too
        results = json_response.get("result")
        return list(map(lambda x: x["postcode"], results))


def get_close_stores(input_data: List[StoreItem], postcode: str, radius: int):
    hash_table_stores = _generate_hash_table(input_data)
    close_postcodes = find_close_postcodes(postcode, radius)
    if close_postcodes:
        matched = [
            hash_table_stores[post]
            for post in close_postcodes
            if post in hash_table_stores.keys()
        ]
        return sorted(matched, key=lambda x: x.location.latitude, reverse=True)
    return []

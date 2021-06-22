from typing import List

import requests

from common.file_handler import process_file_content
from common.models import StoreItem
from task1 import config


def find_close_postcodes(postcode: str, radius: int):

    raw_response = requests.get(f"{config.API_BASE_URL}/postcodes/{postcode}/nearest", params={"radius": radius})
    if raw_response.status_code == 200:
        json_response = raw_response.json()
        # results include the searched post code too
        results = json_response.get("result")
        return list(map(lambda x: x["postcode"], results))


def get_close_stores(hash_table_stores: dict, postcode: str, radius: int):
    close_postcodes = find_close_postcodes(postcode, radius)
    if close_postcodes:
        matched = [hash_table_stores[post] for post in close_postcodes if post in hash_table_stores.keys()]
        return sorted(matched, key=lambda x: x.location.latitude, reverse=True)
    return []


def _generate_hash_table(data: List[StoreItem]) -> dict:
    # performance improvement
    return {item.postcode: item for item in data}

def main():
    # check if file as DB is already generated
    data = process_file_content(config.DATA_PATH)
    validation = {
        "postcode": False,
        "radius": False
    }
    while not validation["postcode"]:
        postcode = input("Please enter postcode:\n")
        if postcode == "q":
            exit()
        if len(postcode) > 6:
            # not sure if the UK postcode could be longer - if I had more time, I'd study it more and used proper regex validation
            validation["postcode"] = True
        else:
            print("You have entered invalid postcode. Try again or write q to end program")

    while not validation["radius"]:
        try:
            # API limits to 1999
            raw_radius = input("Enter radius in decimal metres - maximum 1999:\n")
            if raw_radius == "q":
                exit()
            radius = int(raw_radius)
        except Exception as e:
            # dummy ignore validation
            continue
        if 0 < radius < 2000:
            validation["radius"] = True
        else:
            print("You have entered invalid radius. Try again or write q to end program")

    stores_close_by_postcode = get_close_stores(_generate_hash_table(data), postcode, radius)
    if stores_close_by_postcode:
        print(f"The closest stores to {postcode}:")
        for store in stores_close_by_postcode:
            print(f"{store.name} - {store.postcode}")
    else:
        print(f"No stores found close to {postcode}")

if __name__ == '__main__':
    main()
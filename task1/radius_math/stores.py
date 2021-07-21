import math
from typing import List

from common.models import GpsPosition, StoreItem
from common.zip_code_handler import get_position_for_zip_code


def _haversine(input_position: GpsPosition, store_position: GpsPosition):
    R = 6372800  # Earth radius in meters
    phi1, phi2 = math.radians(input_position.latitude), math.radians(
        store_position.latitude
    )
    dphi = math.radians(store_position.latitude - input_position.latitude)
    dlambda = math.radians(store_position.longitude - input_position.longitude)

    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    )

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def get_close_stores(input_data: List[StoreItem], postcode: str, radius: int):
    postcode_location = get_position_for_zip_code(postcode)
    matched = [
        store
        for store in input_data
        if _haversine(postcode_location, store.location) <= radius
    ]
    return sorted(matched, key=lambda x: x.location.latitude, reverse=True)

import logging
from typing import Union

import requests

from common.models import GpsPosition
from task1 import config

logger = logging.getLogger(__name__)


def _parse_response(raw_response, zip_code: str) -> Union[GpsPosition, bool]:
    if raw_response.status_code == 200:
        json_response = raw_response.json()
        latitude = str(json_response.get("result", {}).get("latitude"))
        longitude = str(json_response.get("result", {}).get("longitude"))
        if longitude is None or latitude is None:
            logger.error(f"Invalid response from server for {zip_code}")
        return GpsPosition(longitude, latitude)
    elif raw_response.status_code == 404:
        return False


def get_position_for_zip_code(zip_code: str) -> GpsPosition:
    # Could be better to use bulk API call, but in the case all postcodes are valid
    logger.info(f"Processing {zip_code}")
    raw_response = requests.get(
        f"{config.API_BASE_URL}/postcodes/{zip_code.replace(' ', '')}"
    )
    parsed = _parse_response(raw_response, zip_code)
    if parsed is False:
        logger.info(f"{zip_code} is probably terminated. Trying to get information...")
        raw_response = requests.get(
            f"{config.API_BASE_URL}/terminated_postcodes/{zip_code.replace(' ', '')}"
        )
        parsed = _parse_response(raw_response, zip_code)
        if not parsed:
            logger.warning(
                f"ZIP code {zip_code} is problematic to get more information. Skipping..."
            )

    if parsed:
        return parsed
    logger.warning(f"ZIP code {zip_code} does not exist.")

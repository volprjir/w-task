import os
import pickle

import pytest
from common.file_handler import process_file_content
from common.models import GpsPosition, StoreItem

from task1.radius_api import get_close_stores as get_close_stores_api
from task1.radius_math import get_close_stores as get_close_stores_math


def _open_pickle(file_path: str):
    with open(file_path, "rb") as f:
        return pickle.load(f)


@pytest.fixture()
def mocked_input():
    path = "../../data/cache.pickle"
    if os.path.isfile(path):
        return _open_pickle(path)
    process_file_content("../../data/stores.json")
    return _open_pickle(path)


@pytest.mark.parametrize(
    "postcode, radius, expected_result",
    [
        (
            "UB4 0TU",
            1999,
            [
                StoreItem(
                    name="Hayes",
                    postcode="UB4 0TU",
                    location=GpsPosition(longitude=-0.397889, latitude=51.51461),
                )
            ],
        ),
    ],
)
def test_find_in_radius_api(postcode, radius, expected_result, mocker, mocked_input):
    mocker.patch("task1.main.process_file_content", return_value=mocked_input)
    res = get_close_stores_api(mocked_input, postcode, radius)
    assert res == expected_result


@pytest.mark.parametrize(
    "postcode, radius, expected_result",
    [
        (
            "UB4 0TU",
            1999,
            [
                StoreItem(
                    name="Hayes",
                    postcode="UB4 0TU",
                    location=GpsPosition(longitude=-0.397889, latitude=51.51461),
                )
            ],
        ),
    ],
)
def test_find_in_radius_math(postcode, radius, expected_result, mocker, mocked_input):
    mocker.patch("task1.main.process_file_content", return_value=mocked_input)
    res = get_close_stores_math(mocked_input, postcode, radius)
    assert res == expected_result

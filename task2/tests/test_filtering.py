import pytest

from common.models import StoreItem
from task2.stores_handler import filter_store

arr = [
    StoreItem("Bracknell", "RG12 1EN"),
    StoreItem("Brentford", "TW8 8JW"),
    StoreItem("Broadstairs", "CT10 2RQ"),
    StoreItem("Newhaven", "BN9 0AG"),
    StoreItem("Orpington", "BR5 3RP"),
    StoreItem("Tunbridge_Wells", "TN2 3FB"),
]


@pytest.fixture()
def mocked_input():
    return arr


@pytest.mark.parametrize(
    "filter, expected_result",
    [
        ("", arr),
        ("hav", [{"name": "Newhaven", "postcode": "BN9 0AG", "location": None}]),
        (
            "br",
            [
                {"name": "Orpington", "postcode": "BR5 3RP", "location": None},
                {"name": "Bracknell", "postcode": "RG12 1EN", "location": None},
                {"name": "Brentford", "postcode": "TW8 8JW", "location": None},
                {"name": "Broadstairs", "postcode": "CT10 2RQ", "location": None},
                {"name": "Tunbridge_Wells", "postcode": "TN2 3FB", "location": None},
            ],
        ),
        ("rg", [{"name": "Bracknell", "postcode": "RG12 1EN", "location": None}]),
    ],
)
def test_filter(filter, expected_result, mocker, mocked_input):
    mocker.patch("task2.stores_handler.process_file_content", return_value=mocked_input)
    res = filter_store(filter)
    assert res == expected_result

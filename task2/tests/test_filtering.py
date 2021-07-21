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
        ("hav", [StoreItem("Newhaven", "BN9 0AG")]),
        (
            "br",
            [
                StoreItem("Orpington", "BR5 3RP"),
                StoreItem("Bracknell", "RG12 1EN"),
                StoreItem("Brentford", "TW8 8JW"),
                StoreItem("Broadstairs", "CT10 2RQ"),
                StoreItem("Tunbridge_Wells", "TN2 3FB"),
            ],
        ),
        ("rg", [StoreItem("Bracknell", "RG12 1EN")]),
    ],
)
def test_filter(filter, expected_result, mocker, mocked_input):
    mocker.patch("task2.stores_handler.process_file_content", return_value=mocked_input)
    res = filter_store(filter)
    assert res == expected_result

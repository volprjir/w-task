from dataclasses import dataclass


@dataclass
class GpsPosition:
    longitude: str
    latitude: str


@dataclass
class StoreItem:
    name: str = None
    postcode: str = None
    location: GpsPosition = None

    def is_empty(self):
        return self.name is None and self.postcode is None

    def __lt__(self, other):
        return self.name < other.name


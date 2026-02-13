from map import Map
from map_description import MapDescription


def test_map_boundaries():
    width = 80
    height = 30
    lines = ["E--------------", "              |", "X------------------"]
    map = Map(MapDescription(lines), width, height)
    assert len(map._matrix) == height, "Matrix exceeds height of {}".format(height)
    for row in map._matrix:
        assert len(row) == width

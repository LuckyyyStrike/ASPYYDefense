from Map import Map
from Map_Description import Map_Description


def test_map_boundaries():
    lines = ["E--------------", "              |", "X------------------"]
    map = Map(Map_Description(lines), 80, 30)
    assert len(map._matrix) == 30
    for row in map._matrix:
        assert len(row) == 80

import pytest
from Map_file_reader import Map_file_reader


@pytest.mark.parametrize(
    "lines, max_width, max_height",
    [
        pytest.param(["E----", "---------X"], 6, 10, id="too many columns"),
        pytest.param(["E----", "---------", "---------X"], 60, 2, id="too many rows"),
    ],
)
def test_raises_out_of_bounds(lines: list[str], max_width: int, max_height: int):
    with pytest.raises(ValueError):
        Map_file_reader(lines, max_width, max_height)


@pytest.mark.parametrize(
    "lines",
    [
        pytest.param(["---\\", "----X"], id="raises with no entry point"),
        pytest.param(["E---\\", "--E--X"], id="raises with too many entry points"),
        pytest.param(["---\\", "----X"], id="raises with no exit point"),
        pytest.param(["E--X\\", "-----X"], id="raises with too many exit points"),
    ],
)
def test_raises_unexpected_semantics(lines: list[str]):
    with pytest.raises(ValueError):
        Map_file_reader(lines, 80, 30)


def test_returns_map_description():
    lines = ["E----", "------", "------X"]
    reader = Map_file_reader(lines, 80, 30)
    # reader = Map_file_reader(lines, 80, 30)
    map_description = reader.create_map_definition()
    assert len(map_description.lines) == 3
    # assert map_description.width == 80
    # assert map_description.height == 30

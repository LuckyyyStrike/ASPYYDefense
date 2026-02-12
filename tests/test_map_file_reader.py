import pytest
from Map_File_Reader import Map_File_Reader


@pytest.mark.parametrize(
    "lines",
    "max_width",
    "max_height",
    [
        pytest.param(["E----", "---------X"], 6, 10, id="too many columns"),
        pytest.param(["E----", "---------", "---------X"], 60, 2, id="too many rows"),
    ],
)
def test_raises_out_of_bounds(lines: list[str], max_width: int, max_height: int):
    with pytest.raises(ValueError):
        Map_File_Reader(lines, max_width, max_height)


@pytest.mark.parametrize(
    "lines",
    [
        pytest.param(["---\\", "----X"], id="no entry point"),
        pytest.param(["E---\\", "--E--X"], id="too many entry points"),
        pytest.param(["---\\", "----X"], id="no exit point"),
        pytest.param(["E---\\", "--X--X"], id="too many exit points"),
    ],
)
def test_raises_unexpected_semantics(lines: list[str]):
    with pytest.raises(ValueError):
        Map_File_Reader(lines, 80, 30)

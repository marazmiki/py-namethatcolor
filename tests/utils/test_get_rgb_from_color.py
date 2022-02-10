import pytest

from py_namethatcolor.utils import get_rgb_for_color


@pytest.mark.parametrize(
    argnames="color, expected",
    argvalues=[
        ("#000000", (0, 0, 0)),
        ("#FF0000", (255, 0, 0)),
    ],
    ids=["black", "red"],
)
def test_get_rgb_for_color_good(color, expected):
    assert get_rgb_for_color(color) == expected


@pytest.mark.parametrize("bad_color", ["#000", "black", "000000"])
def test_get_rgb_for_color_bad(bad_color):
    with pytest.raises(ValueError):
        get_rgb_for_color(bad_color)

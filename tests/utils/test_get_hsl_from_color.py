import pytest

from py_namethatcolor.utils import get_hsl_for_color


@pytest.mark.parametrize(
    argnames="color, expected",
    argvalues=[
        ("#000000", (0, 0, 0)),
        ("#FF0000", (0, 255, 127)),
        ("#00FF00", (85, 255, 127)),
        ("#0000FF", (170, 255, 127)),
    ],
    ids=["black", "red", "green", "blue"],
)
def test_get_hsl_for_color(color, expected):
    assert get_hsl_for_color(color) == expected

import pytest

from py_namethatcolor.models import Rgb


@pytest.mark.parametrize(
    argnames="colors, expected_string",
    argvalues=[
        ((0, 0, 0), "#000000"),
        ((0, 13, 25), "#000D19"),
        ((255, 255, 255), "#FFFFFF"),
    ],
)
def test_as_string(colors, expected_string):
    assert Rgb(*colors).as_string() == expected_string


def test_from_color():
    color = Rgb.from_color("#FF0000")
    assert all(
        (
            color.r == 255,
            color.g == 0,
            color.b == 0,
        )
    )

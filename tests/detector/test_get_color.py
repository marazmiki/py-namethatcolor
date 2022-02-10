import pytest

from py_namethatcolor import get_color


@pytest.mark.parametrize(
    argnames="hex_color, expected_shade_name",
    argvalues=[
        ("#000000", "Black"),
        ("#FFFFFF", "White"),
        ("#0000FF", "Blue"),
        ("#336699", "Blue"),
    ],
)
def test_get_color(hex_color, expected_shade_name):
    color = get_color(hex_color)
    assert color.shade.name == expected_shade_name

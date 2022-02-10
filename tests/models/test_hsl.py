from py_namethatcolor.models import Hsl


def test_from_color():
    hsl = Hsl.from_color("#FF0000")
    assert all(
        (
            hsl.h == 0,
            hsl.s == 255,
            hsl.l == 127,
        )
    )

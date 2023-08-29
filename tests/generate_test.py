"""Tests for the generator"""

from pytest import approx
from generate import Miter, mirror_axis, nudge

points = [
    (approx(0), approx(16.07695155)),
    (approx(10.47197551), approx(14.73720558)),
    (approx(20.94395102), approx(12.05771366)),
    (approx(31.41592653), approx(10.7179677)),
    (approx(41.88790204), approx(12.05771366)),
    (approx(52.35987755), approx(14.73720558)),
    (approx(62.83185306), approx(16.07695155)),
]

full = [
    (approx(0), approx(16.07695155)),
    (approx(20.94395102), approx(12.05771366)),
    (approx(41.88790204), approx(12.05771366)),
    (approx(62.83185306), approx(16.07695155)),
    (approx(62.83185306), approx(-16.07695155)),
    (approx(41.88790204), approx(-12.05771366)),
    (approx(20.94395102), approx(-12.05771366)),
    (approx(0), approx(-16.07695155)),
]

half = [
    (approx(0), approx(16.07695155)),
    (approx(20.94395102), approx(12.05771366)),
    (approx(41.88790204), approx(12.05771366)),
    (approx(62.83185306), approx(16.07695155)),
    (approx(62.83185306), approx(0)),
    (approx(0), approx(0)),
]

full_inverted = [
    (approx(0), approx(10.7179677)),
    (approx(20.94395102), approx(14.73720558)),
    (approx(41.88790204), approx(14.73720558)),
    (approx(62.83185306), approx(10.7179677)),
    (approx(62.83185306), approx(-10.7179677)),
    (approx(41.88790204), approx(-14.73720558)),
    (approx(20.94395102), approx(-14.73720558)),
    (approx(0), approx(-10.7179677)),
]

half_inverted = [
    (approx(0), approx(10.7179677)),
    (approx(20.94395102), approx(14.73720558)),
    (approx(41.88790204), approx(14.73720558)),
    (approx(62.83185306), approx(10.7179677)),
    (approx(62.83185306), approx(0)),
    (approx(41.88790204), approx(0)),
    (approx(20.94395102), approx(0)),
    (approx(0), approx(0)),
]


objects = ()

gap_multiplier = 1.4


def test_miter_points():
    """test the Miter dxf preprocessing"""
    miter = Miter(40, 90, 10, 4, 6)
    lines = miter.curvepoints()
    assert lines == points


def test_end_segment():
    miter = Miter(40, 90, 10, 4, 3)
    end_segment = miter.end_segment()
    assert end_segment == half


def test_full_segment():
    miter = Miter(40, 90, 10, 4, 3)
    full_segment = miter.full_segment()
    assert full_segment == full


# def test_miter_objects():
#     miter = Miter(40, 90, 10, 4, 3)
#     miter_objects = miter.objects()
#     assert miter_objects == objects


def test_nudge():
    points = [(-1, -4), (1, 2), (-4, 4)]
    nudged_points = [(0, -2), (2, 4), (-3, 6)]
    assert nudge(points, (1, 2)) == nudged_points


def test_mirror():
    line = [(1, -1), (-2, 1), (3, 4)]
    mirrored_x = [(-1, -1), (2, 1), (-3, 4)]
    mirrored_y_offset = [(1, 5), (-2, 3), (3, 0)]
    assert mirror_axis(line, "x") == mirrored_x
    assert mirror_axis(line, "y", 2) == mirrored_y_offset

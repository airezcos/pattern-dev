"""Tests for the generator"""

from pytest import approx
from generate import Miter

points = [
    (approx(0), approx(16.07695155)),
    (approx(10.47197551), approx(14.73720558)),
    (approx(20.94395102), approx(12.05771366)),
    (approx(31.41592653), approx(10.7179677)),
    (approx(41.88790204), approx(12.05771366)),
    (approx(52.35987755), approx(14.73720558)),
    (approx(62.83185306), approx(16.07695155)),
]


def test_miter_points():
    """test the Miter dxf preprocessing"""
    miter = Miter(40, 90, 10, 4, 6)
    lines = miter.curvepoints()
    assert lines == points


def test_pass():
    """Always passing test"""
    assert True

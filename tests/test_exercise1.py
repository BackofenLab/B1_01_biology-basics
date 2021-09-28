import pytest
from exercise1 import exercise_3_a, exercise_3_b, exercise_3_c


def test_exercise_3_a():
    test = exercise_3_a()
    assert test["DNA"] == 3
    assert test["RNA"] == 7
    assert test["ncRNA"] == 1
    assert test["mRNA"] == 6
    assert test["UTR"] == 8
    assert test["ORF"] == 11
    assert test["CDS"] == 10


def test_exercise_3_b():
    test = exercise_3_b()
    assert test["DNA"] == 3
    assert test["splicing"] == 1
    assert test["transcription"] == 3
    assert test["ncRNA"] == 3
    assert test["single-cell-organism"] == 2


def test_exercise_3_c():
    a, b, c, d, e = exercise_3_c()
    assert a is False
    assert b is True
    assert c is True
    assert d is False
    assert e is False

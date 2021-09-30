import pytest
from exercise1 import exercise_2_a, exercise_2_b, exercise_2_c, exercise_3_a, exercise_3_b, exercise_3_c


def test_exercise_2_a():
    test = exercise_2_a()
    assert test["bases"] == 1
    assert test["phosphate"] == 2
    assert test["deoxyribose"] == 3
    assert test["guanine"] == 4
    assert test["cytosine"] == 5
    assert test["hydrogen_bond"] == 6
    assert test["adenine"] == 7
    assert test["thymine"] == 8
    assert test["uracil"] == 9
    assert test["backbone"] == 10

def test_exercise_2_b():
    """
    Because of base paring 33% G alo means 33% C.
    100% - 2 * 33% = 34%
    These 34% are divided equally between T and A.
    We therefore have 17% T and 17% A
    """
    test = exercise_2_b()
    assert test["adenine"] == 17
    assert test["cytosine"] == 33
    assert test["guanine"] == 33
    assert test["thymine"] == 17

def test_exercise_2_c():
    pyramidines, purines = exercise_2_c()
    assert sorted(pyramidines) == ["C", "T", "U"]
    assert sorted(purines) == ["A", "G"]

def test_exercise_2_d():

def test_exercise_2_e():

def test_exercise_2_f():

def test_exercise_2_g():

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

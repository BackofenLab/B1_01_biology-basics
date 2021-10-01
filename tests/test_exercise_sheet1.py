import pytest
from exercise_sheet1 import *


def check_none(*args):
    if None in args:
        print("you have not fill in all the fields")
        raise ValueError


def check_zero_in_dict(d):
    val = d.values
    if 0 in val:
        print("you have not fill in all the fields")
        raise ValueError


def test_exercise_1_a():
    a, b, c, d, e, f, g = exercise_1_a()
    check_none(a, b, c, d, e, f, g)
    assert a is True
    assert b is False
    assert c is False
    assert d is False
    assert e is False
    assert f is False
    assert g is False


def test_exercise_1_b():
    a, b, c, d, e, f, g = exercise_1_b()
    check_none(a, b, c, d, e, f, g)
    assert a is False
    assert b is False
    assert c is False
    assert d is False
    assert e is True
    assert f is False
    assert g is True


def test_exercise_1_c():
    a, b, c, d, e, f, g = exercise_1_c()
    check_none(a, b, c, d, e, f, g)
    assert a is True
    assert b is False
    assert c is True
    assert d is False
    assert e is True
    assert f is True
    assert g is False


def test_exercise_1_d():
    a, b, c, d, e, f, g = exercise_1_d()
    check_none(a, b, c, d, e, f, g)
    assert a is True
    assert b is False
    assert c is True
    assert d is False
    assert e is True
    assert f is False
    assert g is False


def test_exercise_1_e():
    a, b, c, d, e, f, g = exercise_1_e()
    check_none(a, b, c, d, e, f, g)
    assert a is False
    assert b is True
    assert c is False
    assert d is True
    assert e is True
    assert f is True
    assert g is False


def test_exercise_2_a():
    answer = exercise_2_a()
    check_zero_in_dict(answer)
    assert answer["bases"] == 1
    assert answer["phosphate"] == 2
    assert answer["deoxyribose"] == 3
    assert answer["guanine"] == 4
    assert answer["cytosine"] == 5
    assert answer["hydrogen_bond"] == 6
    assert answer["adenine"] == 7
    assert answer["thymine"] == 8
    assert answer["uracil"] == 9
    assert answer["backbone"] == 10


def test_exercise_2_b():
    """
    Because of base paring 33% G alo means 33% C.
    100% - 2 * 33% = 34%
    These 34% are divided equally between T and A.
    We therefore have 17% T and 17% A
    """
    answer = exercise_2_b()
    check_zero_in_dict(answer)
    assert answer["adenine"] == 17
    assert answer["cytosine"] == 33
    assert answer["guanine"] == 33
    assert answer["thymine"] == 17


def test_exercise_2_c():
    pyramidines, purines = exercise_2_c()
    assert sorted(pyramidines) == ["C", "T", "U"]
    assert sorted(purines) == ["A", "G"]


def test_exercise_2_d():
    a, b, c, d, e = exercise_2_d()
    check_none(a, b, c, d, e)
    assert a is True
    assert b is True
    assert c is True
    assert d is False
    assert e is True


def test_exercise_2_e():
    a, b = exercise_2_e()
    check_none(a, b)
    assert a is False
    assert b is True


def test_exercise_2_f():
    """
    The carbonatoms in the sugar of the nucleic acid are numbered from 1 to 5.
    In the phosphate-sugar backbone, C5 and C4 are the carbon atoms that connect
    to the phosphate group so that 5' denotes the end of the chain where C5 is the closest
    and 3' denotes the ed where C3 is the closest.
    """
    a, b, c = exercise_2_f()
    check_none(a, b, c)
    assert a is True
    assert b is False
    assert c is False


def test_exercise_2_g():
    def unification(l):
        return sorted([x.upper() for x in l])

    coding, non_coding = exercise_2_g()

    conding, non_coding = unification(coding), unification(non_coding)

    coding_true = unification(["mRNA"])
    non_coding_true = unification(["microRNA", "rRNA", "siRNA", "snoRNA", "tRNA"])

    assert coding == coding_true
    assert non_coding == non_coding_true


def test_exercise_3_a():
    answer = exercise_3_a()
    check_zero_in_dict(answer)
    assert answer["DNA"] == 3
    assert answer["RNA"] == 7
    assert answer["ncRNA"] == 1
    assert answer["mRNA"] == 6
    assert answer["UTR"] == 8
    assert answer["ORF"] == 11
    assert answer["CDS"] == 10


def test_exercise_3_b():
    answer = exercise_3_b()
    check_zero_in_dict(answer)
    assert answer["DNA"] == 3
    assert answer["splicing"] == 1
    assert answer["transcription"] == 3
    assert answer["ncRNA"] == 3
    assert answer["single-cell-organism"] == 2


def test_exercise_3_c():
    a, b, c, d, e = exercise_3_c()
    check_none(a, b, c)
    assert a is False
    assert b is True
    assert c is True
    assert d is False
    assert e is False

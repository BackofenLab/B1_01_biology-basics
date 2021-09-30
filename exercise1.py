def exercise_2_a():
    """Exercise 2 a
    Assign the numbers (1-10) in the figure (see GitHub Readme or figures/sheet1-q2.png) to
    the respective terms given in the following dictionary:
    """
    a = {
        "hydrogen_bond" : 0,
        "phosphate" : 0,
        "adenine" : 0,
        "cytosine" : 0,
        "uracil" : 0,
        "backbone" : 0,
        "deoxyribose" : 0,
        "guanine" : 0,
        "bases" : 0,
        "thymine" : 0,
    }
    return a

def exercise_2_b():
    """Exercise 3 b
    A piece of DNA contains 33% guanine.
    What are the percentages of adenine, cytosine, and thymine in that piece of DNA?
    Assign the percentages of each base to the following dictionary (in integer representation).
    """
    b = {
        "adenine" : 0,
        "cytosine" : 0,
        "guanine" : 33,
        "thymine" : 0
    }
    return b

def exercise_2_c():
    """Exercise 2 c
    Which of the bases are pyramidenes and which are purines?
    Add the nucleotide representation of each base
    (A for adenine, C for cytosine, G for guanine, T for thymine, U for uracil)
    to the correct list.
    """
    bases = ["A", "C", "G", "T", "U"]
    pyramidines = []
    purines = []
    return pyramidines, purines

def exercise_2_d():
    """Exercise 2 d
    Which of these statements concerning DNA and RNA are true and which are false?
    Change the respective variable values accordingly.
    """

    # Uracil is a standard base in RNA
    a = None

    # DNA is longer than RNA
    b = None

    c = None

    d = None

    e = None

    return a, b, c, d, e

def exercise_2_e():
    """Exercise 2 e

    """

def exercise_2_f():
    """Exercise 2 f
    """

def exercise_2_g():
    """Exercise 2 g
    """

def exercise_3_a():
    """Exercise 3 a
    The function contains a dict with acronyms that you should know.
    What do they stand for?
    Enter the number of the correct answer from the list below in the dict


     1: non-coding-RNA
     2: Opposite-Reading-Frame
     3: Deoxyribonucleic acid
     4: non-complementary-RNA
     5: missense-RNA
     6: messenger-RNA
     7: ribonucleic acid
     8: untranslated region
     9: coding-strand
    10: coding-sequence
    11: open reading frame
    """
    a = {
        "DNA": 0,
        "RNA": 0,
        "ncRNA": 0,
        "mRNA": 0,
        "UTR": 0,
        "ORF": 0,
        "CDS": 0,
    }
    return a


def exercise_3_b():
    """Exercise 3 b
    Check whether the following terms belong to Eukaryotes (1), Prokaryotes (2)
    or both (3).
    e.g. DNA: 3
    """
    b = {
        "DNA": 0,
        "splicing": 0,
        "transcription": 0,
        "ncRNA": 0,
        "single-cell-organism": 0,
    }
    return b


def exercise_3_c():
    """Exercise 3 c
    Check whether the  following statements are True or False. Enter your
    answer by changing the variable value accordingly.
    e.g. a = True
    """

    "The genome is stored in the nucleus"
    a = None

    "FASTA files are used to store sequence information"
    b = None

    "A Watson-Crick base pair describes a pyrimidine pairing with a purine"
    c = None

    "A Watson-Crick base pair describes a purine pairing with a purine"
    d = None

    "RNA is a single stranded bio-polymer"
    e = None

    return a, b, c, d, e

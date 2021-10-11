def exercise_1_a():
    """
    Exercise 1 a
    Where is the genome stored in prokaryotes and eukaryotes?
    Assign the correct True and False values to the provided options.
    """

    # Inside the nucleus in eukaryotes
    a = None

    # Outside the cell in prokaryotes
    b = None

    # Prokaryotes have no genome
    c = None

    # Inside the nucleolus in prokaryotes
    d = None

    # In chromatin in eukaryotes
    e = None

    # Partially in mitochondria in prokaryotes
    f = None

    # Inside the nucleoid in eukaryotes
    g = None

    return a, b, c, d, e, f, g


def exercise_1_b():
    """
    Exercise 1 b
    Name two more differences between prokaryotes and eukaryotes?
    Assign the correct True and False values to the provided options.
    """

    # Prokaryotes have compartmentation through membrane
    a = None

    # Eukaryotes are not multi - cellular organisms
    b = None

    # Prokaryotes have mitochondria
    c = None

    # Eukaryotes have no nucleus
    d = None

    # Prokaryotes have no ER
    e = None

    # Eukaryotes are single cell organisms
    f = None

    # Eukaryotes have no flagellum
    g = None

    return a, b, c, d, e, f, g


def exercise_1_c():
    """
    Exercise 1 c
    Name examples for an organism for prokaryotes and eukaryotes.
    Assign the correct True and False values to the provided options.
    """

    # Escherichia coli is a prokaryote
    a = None

    # Amoebas  are prokaryotes
    b = None

    # Fungi are eukaryotes
    c = None

    # Archaea are eukaryotes
    d = None

    # Insects are eukaryotes
    e = None

    # Salmonella is a prokaryote
    f = None

    # Plasmodium  malariae is a prokaryote
    g = None

    return a, b, c, d, e, f, g


def exercise_1_d():
    """
    Exercise 1 d
    Which of these are three information-carrying biopolymers?
    Assign the True and False values to the provided options.
    """

    # Protein
    a = None

    # Cellulose
    b = None

    # DNA
    c = None

    # Polysaccharides
    d = None

    # RNA
    e = None

    # amino acid
    f = None

    # nucleotide
    g = None

    return a, b, c, d, e, f, g


def exercise_1_e():
    """
    Exercise 1 e
    What is denoted by the “Central Dogma” of molecular biology?
    Assign the True and False values to the provided options.
    """

    # Protein can make Protein
    a = None

    # DNA can make DNA
    b = None

    # Protein can make RNA and then RNA makes DNA
    c = None

    # DNA can make RNA and then RNA makes Protein
    d = None

    # RNA can make RNA
    e = None

    # DNA can make RNA and then RNA makes DNA
    f = None

    # Protein can make DNA
    g = None

    return a, b, c, d, e, f, g


def exercise_2_a():
    """
    Exercise 2 a
    Assign the numbers (1-10) in the figure (see GitHub Readme or figures/sheet1-q2.png) to
    the respective terms given in the following dictionary:
    """
    a = {
        "hydrogen_bond": 0,
        "phosphate": 0,
        "adenine": 0,
        "cytosine": 0,
        "uracil": 0,
        "backbone": 0,
        "deoxyribose": 0,
        "guanine": 0,
        "bases": 0,
        "thymine": 0,
    }
    return a


def exercise_2_b():
    """
    Exercise 2 b
    A piece of DNA contains 33% guanine.
    What are the percentages of adenine, cytosine, and thymine in that piece of DNA?
    Assign the percentages of each base to the following dictionary (in integer representation).
    """
    b = {
        "adenine": 0,
        "cytosine": 0,
        "guanine": 33,
        "thymine": 0
    }
    return b


def exercise_2_c():
    """
    Exercise 2 c
    Which of the bases are pyrmidenes and which are purines?
    Add the nucleotide representation of each base
    (A for adenine, C for cytosine, G for guanine, T for thymine, U for uracil)
    to the correct list.
    """
    bases = ["A", "C", "G", "T", "U"]
    pyrimidines = []
    purines = []
    return pyrimidines, purines


def exercise_2_d():
    """
    Exercise 2 d
    Which of these statements concerning DNA and RNA are true and which are false?
    Change the respective variable values with True or False accordingly.
    """

    # Uracil is a standard base in RNA
    a = None

    # DNA is longer than RNA
    b = None

    # DNA and RNA have a different structure
    c = None

    # RNA has an intermolecular double-helix structure
    d = None

    # RNA contains ribose sugar
    e = None

    return a, b, c, d, e


def exercise_2_e():
    """
    Exercise 2 e
    In what direction is an RNA sequence written ?
    Change the respective variable values with True or False accordingly.
    """

    # 3' end to 5' end
    a = None

    # 5' end to 3' end
    b = None

    return a, b


def exercise_2_f():
    """
    Exercise 2 f
    Why is the RNA sequence written in that diretion?
    Change the respective variable values with True or False accordingly.
    """

    # The order is based on the numbering of the carbons in the sugar of the nucleic acid
    a = None

    # The order is based on the numbering of the carbons in the phosphate of the nucleic acid
    b = None

    # The order was arbitrarily chosen by the discoverer of RNA
    c = None

    return a, b, c


def exercise_2_g():
    """
    Exercise 2 g
    Decide for the following RNAs whether they are coding or non-coding
    by adding them to the correct list.
    mRNA, tRNA, rRNA, microRNA, siRNA, snoRNA
    """

    rna_types = ["tRNA", "rRNA", "microRNA", "mRNA", "siRNA", "snoRNA"]
    coding = []
    non_coding = []

    return coding, non_coding


def exercise_3_a():
    """
    Exercise 3 a
    What do these acronyms stand for within this course?
    Enter the number of the correct answer from the list below in the dictionary


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
    """
    Exercise 3 b
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
    """
    Exercise 3 c
    Check whether the  following statements are True or False. Enter your
    answer by changing the variable value accordingly.
    e.g. a = True
    """

    # The genome is stored in the nucleus
    a = None

    # FASTA files are used to store sequence information
    b = None

    # A Watson-Crick base pair describes a pyrimidine pairing with a purine
    c = None

    # A Watson-Crick base pair describes a purine pairing with a purine
    d = None

    # RNA is a single stranded bio-polymer
    e = None

    return a, b, c, d, e


########################################################
############## Programming tasks #######################
########################################################

from helpers.helpers import translation_table


def transcription(dna_string):
    rna_string = None
    return rna_string


def translation(rna_string):
    protein = None
    return protein


def central_dogma(dna_seq):
    protein = None
    return protein

from helpers.helpers import translation_table


def transcription(dna_string):
    """
    Implement the transcription function which takes a DNA sequence as an input and returns the corresponding
    RNA sequence.
    Assume that the provided DNA sequence will be an uppercase string containing only the correct characters
    (from the domain "AGCT"). The function output RNA sequence also has to be in the upper case.
    """
    rna_string = None
    return rna_string


def translation(rna_string):
    """
     Implement the translation function which takes an mRNA sequence and produces the corresponding protein sequence.
     Assume that the provided RNA sequence will be an uppercase string containing only the correct characters
     (from the domain "AGCU"). Assume that the sequence starts with the start codon (AUG) and ends with one of the
     end codons. It does not have any end codons in the middle.The number of characters in the input RNA sequence is
     a multiple of three.
     The function output sequence also has to be in the upper case protein sequence. To make it easier for you,
     we provided you with the translation table which is represented as a python dictionary. You can translate a
     single codon by simply using it:

     translation_table["AUG"]
    """
    protein = None
    return protein


def central_dogma(dna_seq):
    """
    Combine the functions you implemented for the tasks a) and b) and obtain the central dogma function which
    gives you the protein sequence with a given DNA.
    """
    protein = None
    return protein

Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

Course ILIAS web page: *https://ilias.uni-freiburg.de/ilias.php?ref_id=2339316&cmdClass=ilobjcoursegui&cmd=view&cmdNode=zf:ns&baseClass=ilRepositoryGUI*

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 1: Biology basics - DNA/RNA
---

### _Exercise 4 - Programming assignment: Transcription and Translation_
**a)** Implement the transcription function which takes a DNA sequence as an input and returns the corresponding RNA sequence.


Assume that the provided DNA sequence will be an uppercase string containing only the correct characters (from the domain "AGCT").
The function output RNA sequence also has to be in the upper case.

**b)** Implement the translation function which takes an mRNA sequence and produces the corresponding protein sequence.

Assume that the provided RNA sequence will be an uppercase string containing only the correct characters (from the domain "AGCU").
Assume that the sequence starts with the start codon (AUG) and ends with one of the end codons. It does not have any end codons in the middle.The number of characters in the input RNA sequence is a multiple of three.

The function output sequence also has to be in the upper case protein sequence.
To make it easier for you, we provided you with the translation table which is represented as a python dictionary. 
You can translate a single codon by simply using it:

```
translation_table["AUG"]

```
**c)** Combine the functions you implemented for the tasks **a)** and **b)** and obtain the central dogma function which gives you the protein sequence with a given DNA.

All the assumptions about the inputs and output are similar to the tasks **a)** and **b)**.

---

#### Recommended good practices

Here we have included some best practices helping you solve the exercises as efficiently as possible. First, clone the assignment repository.
    

```
$ git clone git@github.com:Bioinformatics-teaching/01_biology-basics-userID.git
```

Do not forget to use your own user ID. Now, answers the questions.


```
$ cd 01_biology-basics-userID
$ emacs -nw exercise_sheet1.py
```

Include the changes and make a commit describing the modifications.


```
$ git add exercise_sheet1.py
$ git commit -m "Description of your modifications"
```

 
Send your results.       


```
$ git push
```

Done! But, it would be nice to know something about the score, wouldn't it? Let's check the autograding results. This PR will also be used by the teachers to include specific comments.


<img src="./figures/sheet2_classroom.gif" alt="Autograding" width=100%/>


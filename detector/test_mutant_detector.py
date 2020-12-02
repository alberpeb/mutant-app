from mutant_detector import is_mutant

humans = ([
    "ATGCGA",
    "CAGTGC",
    "TTATTT",
    "AGACGG",
    "GCGTCA",
    "TCACTG"
],
[
    "ATCGTAG",
    "CTAGTCG",
    "TAGTTGG",
    "CTAGTCT",
    "TAAGGCG",
    "CAGTCAG",
    "CGGTCAG",
],
[
    "ATCGTAG",
    "CTAGTCG",
    "TAGTTCG",
    "CTATTTT",
    "TAAGGCG",
    "CAGTCAG",
    "CGGTCAG",
],
[
    "ATCGTAG",
    "CTAGTCG",
    "TAGTTCG",
    "CTAGTGT",
    "TAAGGCG",
    "CAGTCAG",
    "CGGTCAG",
],
[
    "ATCGTAG",
    "CTAGTCG",
    "TAGTTCG",
    "CTAGTAT",
    "TAATGCG",
    "CATTCAG",
    "CTGTCAG",
])

mutants = ([
    "ATGCGA",
    "CAGTGC",
    "TTATGT",
    "AGAAGG",
    "CCCCTA",
    "TCACTG"
],
[
    "ATGCGA",
    "CAGTGC",
    "ATATGC",
    "TTAACG",
    "CCACTA",
    "TCCATG"
],
[
    "ATGCGA",
    "CAGTGC",
    "TCATGT",
    "AGCAGG",
    "CCTCTA",
    "TCACTG"
],
[
    "ATCCACTA",
    "ATTCAACC",
    "CAGTACAT",
    "TTATATGG",
    "AGAATAGA",
    "CTCCTACC",
    "TCACTGTT",
    "TCACTGGT"
],
[
    "ATCCCC",
    "CAGTGC",
    "TTATTT",
    "AGAAGG",
    "CACTTA",
    "ACACTG"
])

def test_human():
    #assert is_mutant(humans[0]) == False
    assert is_mutant(humans[1]) == False
    assert is_mutant(humans[2]) == False
    assert is_mutant(humans[3]) == False
    assert is_mutant(humans[4]) == False

def test_mutant():
    assert is_mutant(mutants[0]) == True
    assert is_mutant(mutants[1]) == True
    assert is_mutant(mutants[2]) == True
    assert is_mutant(mutants[3]) == True
    assert is_mutant(mutants[4]) == True

if __name__ == '__main__':
    test_human()
    test_mutant()
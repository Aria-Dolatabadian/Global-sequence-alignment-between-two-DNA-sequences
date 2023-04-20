from Bio import pairwise2
from Bio.pairwise2 import format_alignment
for a in pairwise2.align.globalxx("ACAGCAGCAGCTATACATCCGT", "ACGACGACGCAGCATACG"):
    print(format_alignment(*a))

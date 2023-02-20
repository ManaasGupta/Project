from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import *
human_record=SeqIO.parse('HBB-hs.fasta','fasta')
rat_record=SeqIO.parse('Hb-rat.fasta','fasta')
for element in human_record:
    humanHBB=str(element.seq)
for element in rat_record:
    ratHBB=str(element.seq)
print(humanHBB)
print('\n')
print(ratHBB)
print('\n')
#global alignment
# print(help(pairwise2.align.globalxx))
global_alignment=pairwise2.align.globalxx(humanHBB,ratHBB)
print(global_alignment[0])
print('\n')
print(format_alignment(*global_alignment[0]))
print('\n')
for ind,pair in enumerate(global_alignment):
    print(format_alignment(*global_alignment[ind]))

#local alignment

local_alignment=pairwise2.align.localmx(humanHBB,ratHBB,2,0)
print(format_alignment(*local_alignment[0]))
for ind,pair in enumerate(local_alignment):
    print(format_alignment(*local_alignment[ind]))
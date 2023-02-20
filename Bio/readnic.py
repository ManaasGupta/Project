from Bio import Phylo
readTree=Phylo.read('HBB.ph','newick')
print(readTree)
Phylo.draw_ascii(readTree)
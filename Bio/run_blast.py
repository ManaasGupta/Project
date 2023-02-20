from Bio import SeqIO
from Bio.Blast import NCBIWWW
record=SeqIO.parse('HBB-hs.fasta','fasta')
seq=''
for element in record:
    seq=element.seq
# print(seq)

blast_command=NCBIWWW.qblast(program='blastn',database='nt',sequence=seq)
with open ('blastresults.xml','w+') as w:
    w.write(blast_command.read())
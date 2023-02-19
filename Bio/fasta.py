from Bio import SeqIO

fasta=SeqIO.parse('seqdump.txt','fasta')
for ele in fasta:
    print(ele.id)
    print(ele.seq)

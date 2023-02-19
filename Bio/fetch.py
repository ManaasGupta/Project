from Bio import Entrez as ent
ent.email='manasgpt3@gmail.com'
# 3 examples of Homo sapiens Genes
# HBB : hemoglobin subunit beta
# DNASE1L3 : dioxyribonuclease 1 like 3
# OCA2 : OCA2 melansomal transmembrane protein (green eye color)
record=ent.read(ent.esearch(db='nucleotide',term='HBB[Gene Name] AND Homo sapiens[Organism] AND  RefSeq[Keyword]', retmax=100,idtype='acc'))
print(record)
counter=0
fetchlist=[]
for id in record['IdList']:
    if 'NM_' in id:
        counter +=1
        fetch=ent.efetch(db='nucleotide',id=id,rettype='gb',retmode='text')
        readfetch=fetch.read()
        fetchlist.append(readfetch)
        # print(readfetch)
# print(counter)
print(len(fetchlist))
for files in fetchlist:
    with open('HBB-hs-gb.gb','a+') as savedfile:
        savedfile.write(files)
print('HBB-hs.fasta Downlaoded')

'''
NM_ : mRNA
NC_ : Genomic Data
XM_ : predicted mRNA
NT_ : Nucleotide collection 
NR_ : Amino Acids 

'''
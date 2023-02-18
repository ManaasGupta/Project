from Bio import Entrez as ent
ent.email='manasgpt3@gmail.com'
record=ent.read(ent.espell(db='pmc',term='biopython'))
print(type(record))
print(record.keys())
for key in record.keys():
    print(key,':',record[key])
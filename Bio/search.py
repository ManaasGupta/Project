from Bio import Entrez as ent
ent.email='manasgpt3@gmail.com'
db=ent.read(ent.esearch(db='pmc',term='biopython',retmax=2800))
print(type(db))
print(db.keys())
for key in db.keys():
    print(key,':',db[key])

bioID=db['IdList']
print(bioID)

for ID in bioID[:10]:
    summary=ent.read(ent.esummary(db='pmc',id=ID))
    for handle in summary:
        print(handle['Title'],'\t',handle['FullJournalName'],'\t',handle['DOI'],'\n')

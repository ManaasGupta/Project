from Bio import Entrez as ent
ent.email='manasgpt3@gmail.com'
db=ent.read(ent.einfo())
print(type(db))
print(db.keys())
print('.\n'.join(sorted(db['DbList'])))

db=ent.read(ent.einfo(db='genome'))
print(type(db))
print(db.keys())
for key in db['DbInfo'].keys():
    print(key,':',db['DbInfo'][key] )

from Bio import Entrez as ent
ent.email = 'learnbiopython@gmail.com' 
r = ent.read(ent.esearch(db='nucleotide', term='INS[Gene Name] AND RefSeq[Keyword]', retmax=10000, idtype='acc'))
counter=0
fetchlist=[]
for id in r['IdList']:
    if 'NM_' in id:
        counter +=1
        fetch=ent.efetch(db='nucleotide',id=id,rettype='gb',retmode='text')
        readfetch=fetch.read()
        fetchlist.append(readfetch)
        # print(readfetch)
# print(counter)
print(len(fetchlist))
for files in fetchlist:
    with open('INS.gb','a+') as savedfile:
        savedfile.write(files)
print('INS.fasta Downlaoded')
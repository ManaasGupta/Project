from Bio import SeqIO 
from Bio.Seq import *
from Bio.SeqRecord import *
from Bio.SeqFeature import *
record=SeqIO.parse('HBB-hs.fasta','fasta')
for element in record:
    # print(element)
    # print('\n'),
    f1=SeqFeature(FeatureLocation(0,628,strand=1),type='gene')
    newRecord=SeqRecord(Seq(str(element.seq)),id=element.id, description=element.description,name=element.name,annotations=element.annotations['molecule_type'],features=[f1])
    print(newRecord.format('genbank'))
    # with open ('INSg.gb','w') as f:
    #     f.write(newRecord.format('genebank'))
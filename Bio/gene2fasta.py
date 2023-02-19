from Bio import SeqIO as seqe
from Bio.Seq import *
from Bio.SeqRecord import *
record=seqe.parse('HBB-hs-gb.gb','gb')
for element in record:
    print(element)
    print('\n')
    newRecord=SeqRecord(Seq(str(element.seq)),id=element.id, description=element.description,name=element.name)
    print(newRecord.format('fasta'))
    print(element.annotations)
    with open ('INS.fasta','w') as f:
        f.write(newRecord.format('fasta'))
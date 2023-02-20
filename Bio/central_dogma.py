from Bio import SeqIO
from Bio.Seq import *
record=SeqIO.parse('HBB-hs.fasta','fasta')
c_count=0
i_count=0
c_index=[]
i_index=[]
for element in record:
    dnaSeq=str(element.seq)
    print('DNA Sequence \n',str(element.seq))
    rnaSeq=transcribe(dnaSeq)
    print('RNA Sequence \n',rnaSeq)
    print('DNA Sequence using back transcribe \n',back_transcribe(rnaSeq))
    com=complement(dnaSeq)
    print('Compliment DNA Sequence\n',com)
    aaSeq=translate(dnaSeq,table=1)
    aaSeq1=translate(dnaSeq,table=2)
    print('Amino Acid Sequence \n',aaSeq)
    print('Amino Acid Sequence from Mitochondrial \n',aaSeq1)
    print(len(aaSeq))
    print(len(aaSeq1))

    for i in range(0,len(aaSeq)):
        if aaSeq[i]==aaSeq1[i]:
            c_count +=1
            c_index.append(i)
        else:
            i_count +=1
            i_index.append(i)
print((c_count,i_count))
print('Same index',c_index)
print('Dissimilar index',i_index)
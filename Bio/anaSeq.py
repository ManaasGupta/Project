from Bio import SeqIO
from Bio.SeqUtils import *
from Bio.Seq import *
record=SeqIO.parse('HBB-hs.fasta','fasta')
c_count=0
i_count=0
c_index=[]
i_index=[]
for element in record:
    print(element.seq)
    dnaSeq=str(element.seq)
    # print('DNA Sequence \n',str(element.seq))
    rnaSeq=transcribe(dnaSeq)
    aaSeq=translate(dnaSeq,stop_symbol='')
    print(aaSeq)
    gc_content=GC(dnaSeq)
    print(gc_content)
    atg_posi=nt_search(dnaSeq,'ATG')
    print(atg_posi)
    mol_weight=molecular_weight(aaSeq,'protein')
    print(mol_weight)
    six_frame=six_frame_translations(dnaSeq)
    print(six_frame)
    aa_3letter=seq3(aaSeq)
    print(aa_3letter)
    aa1=seq1(aa_3letter)
    print(aa1)
    print((len(aaSeq),len(aa1)))
    for i in range(0,len(aaSeq)):
        if aaSeq[i]==aa1[i]:
            c_count +=1
            c_index.append(i)
        else:
            i_count +=1
            i_index.append(i)
print((c_count,i_count))
print('Same index',c_index)
print('Dissimilar index',i_index)
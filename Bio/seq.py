from Bio import SeqIO
record=SeqIO.parse('HBB-hs.fasta','fasta')
index_a=[]
index_t=[]
index_g=[]
index_c=[]
nan=0
for element in record:
    print(str(element.seq))
    print(str(element.seq.count('ATG')))
    print(str(element.seq.find("ATG")))
    print(len(str(element.seq)))
    print(str(element.seq).lower())
    print('\n')
    print(str(element.seq).upper())
    print('\n')
    print(str(element.seq).replace('T','U'))
    
    for i in range(0,len(str(element.seq))):
        if element.seq[i]=='A':
            index_a.append(i)
        elif element.seq[i]=='T':
            index_t.append(i)
        elif element.seq[i]=='G':
            index_g.append(i)
        elif element.seq[i]=='C':
            index_c.append(i)
        else:
            nan += 1
print("A's Position: ",index_a,"and number of As in sequence",element.seq.count('A'))
print("T's Position: ",index_t,"and number of Ts in sequence",element.seq.count('T'))
print("G's Position: ",index_g,"and number of Gs in sequence",element.seq.count('G'))
print("C's Position: ",index_c,"and number of Cs in sequence",element.seq.count('C'))
print("Number of non Identified Nucleotide: ",nan)
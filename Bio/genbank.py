from Bio import SeqIO as seqe
record=seqe.parse('HBB-hs-gb.gb','gb')
for ele in record:
    print(ele.name)
    print(ele.description)
    print(ele.seq)
    for key in ele.annotations:
        print(key,':',ele.annotations[key])
    print(ele.features)
    for feature in ele.features:
        print(feature,feature.location)
        print('\n')

r=seqe.parse('INS.gb','gb')
for ele in r:
    print(ele.annotations['organism'])
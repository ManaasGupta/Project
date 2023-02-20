from Bio.Blast import NCBIXML
record=NCBIXML.read(open('blastresults.xml'))
for ind,align in enumerate(record.descriptions):
    print('Alignment Index: ',ind)
    print('Title: ',align.title)
    print('Score: ',align.score)
    print('Evalue: ',align.e)
    
for ind,align in enumerate(record.alignments):
    print(('...'))
    print('Alignment Index: ',ind)
    print('1.) Title: ',align.title)
    print('2.) Length: ',align.length)
    print('3.) HSP: ',align.hsps)
    for hsp in align.hsps:
        print('3.1.) Score',hsp.score)
        print('3.2.) 2 Bits',hsp.bits)
        print('3.3.) e-Vlaue',hsp.expect)
        print('3.4.) Identities',hsp.identities)
        print('3.5.) Gaps',hsp.gaps)
        print('3.6.) Strand',hsp.strand)
        print('3.7.) Frame',hsp.frame)
        print('3.8.) Query Strand',hsp.query_start)
        print('3.9.) Subject',hsp.sbjct_start)
        print('3.10.) Alignment Length',hsp.align_length)
        print(hsp.query[:])
        print(hsp.match[:])
        print(hsp.sbjct[:])

from Bio.Align.Applications import ClustalwCommandline
# print(help(ClustalwCommandline))
cmd=ClustalwCommandline('C:\Program Files (x86)\ClustalW2\clustalw2',infile='HBB.fasta',type='DNA'
                        ,clustering='NJ',outfile='HBBc.fasta')
std_out,std_err=cmd()
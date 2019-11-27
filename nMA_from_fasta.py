'''
Create a numbered master alignment from a fasta file of protein sequences to use
in the compare_aa_distribution.py pipeline

Dependencies
	- MAFFT ( conda install -c bioconda mafft )

Usage:
	python nMA_from_fasta.py <fasta_with_protein_sequences> <output_name>

Workflow:
	1. Using MAFFT, align all protein sequences in the input fasta file together
	2. Convert multi-line fasta to single-line fasta
	3. Number each non-gap position within each read with its position within
		the entire alignment.

Output
	- Similar to a normal fasta file, but with a third line containing position
		information relative to the master alignment

To-do
	- Allow user to go from MA to nMA, in case they already have master alignment
		or the process fails mid run, as the MA generation takes awhile

-Z
'''

from sys import argv
import subprocess


def fasta_fixer(input_file,output_file):
	'''Reformat fasta file to remove newline characters within sequence

	Keyword arguments:
		input -- fasta file to fix location
		output -- fixed fasta file location
	
	'''
	out = open(output_file,'w')

	for i,l in enumerate(open(input_file,'U')):
		if l[0] == '>':
			if i == 0:
				out.write(l)
			else:
				out.write('\n'+l)
		else:
			out.write(l.strip())
	out.close()
	


input_fasta = argv[1]
output_nMA_name = argv[2]

MA = input_fasta.split('.fa')[0] + '_MA.txt'

subprocess.call("mafft %s > %s" % (input_fasta, MA), shell = True)
fixed_MA = input_fasta.split('.fa')[0] + '_fixed.fasta'
fasta_fixer(MA, fixed_MA)

nMA_out = open(output_nMA_name, 'w')

for l in open(fixed_MA, 'U'):
	if l.startswith('>'):
		nMA_out.write(l)
	else:
		sequence_list = []
		index_list = []
		for i, pos in enumerate(l):
			if pos != '-':
				sequence_list.append(pos)
				index_list.append(str(i + 1))
		nMA_out.write("".join(sequence_list))
		nMA_out.write(",".join(index_list) + '\n')

nMA_out.close()





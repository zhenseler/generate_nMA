# generate nMA

Create a numbered master alignment from a fasta file of protein sequences to use
in the compare_aa_distribution.py pipeline

##Dependencies

	- MAFFT ( conda install -c bioconda mafft )

##Usage:

	python nMA_from_fasta.py <fasta_with_protein_sequences> <output_name>

##Workflow:

	1. Using MAFFT, align all protein sequences in the input fasta file together
	2. Convert multi-line fasta to single-line fasta
	3. Number each non-gap position within each read with its position within
		the entire alignment.

##Output

	- Similar to a normal fasta file, but with a third line containing position
		information relative to the master alignment

##To-do

	- Allow user to go from MA to nMA, in case they already have master alignment
		or the process fails mid run, as the MA generation takes awhile

-Z

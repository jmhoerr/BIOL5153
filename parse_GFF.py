#! /usr/bin/env python3

import csv
import argparse
import re 
from Bio import SeqIO
from collections import defaultdict

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome.')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# dictionary: key = gene_name, value = sequence
gene_dict = defaultdict(dict)


# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
# print(genome.id)
# print(genome.seq)



# open and read in GFF file
with open(args.gff, 'r') as gff_in:
	
	# create a CSV reader object
	reader = csv.reader(gff_in, delimiter='\t') 

	# loop over all the lines in our reader object (i.e., parsed file)
	for line in reader:
		header = line[8]
		start  = line[3]
		end    = line[4]
		strand = line[6]
		code   = line[2]
		
		# print gene name 
		header_split = header.split()
		gene_name = 'Citrullus_lanatus_' + header_split[1]
		exon_num = header_split[3]
				
					
		# extract CDS from code list
		if code == 'CDS':
			
			# calculate and return reverse complement of features on '-' strand
			if strand == '+':
				pos_strand = genome.seq[int(start)-1:int(end)]
				print(gene_name)
				print(pos_strand)
				

			else:
				neg_strand = genome.seq[int(start)-1:int(end)]
				rev_comp = neg_strand.reverse_complement()
				print(gene_name)
				print(rev_comp)
			
		else:
			continue


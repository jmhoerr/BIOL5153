#! /usr/bin/env python3

# Assignment 5: calculating nucleotide composition of nad4L

# set the name of input DNA sequence file
filename = 'dna.txt'

# open the input file, assign to file handle called 'infile'
infile = open(filename, 'r')

# read the file
dna_sequence = infile.read().rstrip()

# print the DNA sequence
print(dna_sequence)

# close the file
infile.close()

# calculate total length
seqlen = len(dna_sequence)
print('Sequence length:', seqlen)

# count bases
numA = dna_sequence.count('A')
numT = dna_sequence.count('T')
numC = dna_sequence.count('C')
numG = dna_sequence.count('G')

# calculate frequencies
freqA = numA / seqlen
freqT = numT / seqlen
freqC = numC / seqlen
freqG = numG / seqlen
GC_content = freqG + freqC

# check frequencies sum to 1
total_sum = freqA + freqT + freqC + freqG
print(total_sum)

# write output to STDOUT
outfile = STDOUT
outfile.write('Sequence length: ' + str(seqlen))
outfile.write('Freq of A: ' + str(freqA))
outfile.write('Freq of C: ' + str(freqC))
outfile.write('Freq of G: ' + str(freqG))
outfile.write('Freq of T: ' + str(freqT))
outfile.write('GC content: ' + str(GC_content))

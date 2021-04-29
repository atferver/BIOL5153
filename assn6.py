#! /usr/bin/env python3
import re
import csv
import argparse
from Bio import SeqIO
#from Bio.Alphabet import generic_dna

# inputs: 1) GFF file, 2)corresponding genome sequence

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
#print(genome.id)
#print(len(genome.seq))

# read in GFF file
with open(args.gff, 'r') as gff_in:

    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')
    # loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
		# skip blank lines
        if(not line):
            continue

		# skip comment lines
        elif(re.search('^#', line[0])):
            continue

		# else it's a data line
        else:
            feature = line[2]
            start   = line[3]
            end     = line[4]
            strand  = line[6]
            attributes = line[8]
			# extract the sequence
fragment = genome.seq[int(start)-1:int(end)]


print('>' + genome.id + ' ' + line[8])
print(fragment)

from contextlib import redirect_stdout

with open('assn6.fasta', 'w') as f:
    with redirect_stdout(f):
        print('>' + genome.id + ' ' + line[8])
        print(fragment)

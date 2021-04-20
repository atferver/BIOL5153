#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

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
print(genome.id)
print(len(genome.seq))

# read in GFF file
with open(args.gff, 'r') as gff_in:

    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')
    # loop over all the lines in our reader object file (i.e., parsed file)
    for line in reader:
        start  = line[3]
        end    = line[4]
        strand = line[6]
        
        print(len(genome.seq))




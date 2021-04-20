#! /usr/bin/env python3

#import modules 
import csv
from collections import defaultdict

# dictionary key = president number, value = president name
presidents = defaultdict(dict)
# dictionary key = party name, value = number of presidents in that party
party = defaultdict(dict)

#  open and parse the data file
with open('presidents.csv', 'r') as infile:
    # create a csv reader object
    reader = csv.reader(infile, delimiter=',')

    # loop over each line in reader
    for line in reader:
        # skip header line
        if(line[0] == 'Presidency '):
            continue
        # else its a data line -- parse this
        else:
            presidents[line[0]] = line[1]
            party[line[5]] = line[1]

for i in party.keys():
    print(i, party[i])
#this has many errors becasue of spaces being added before and after in some cases
#it alos only gives the name of the last time the party was seen in the dictionary
#print('President #16 was', presidents.get('16'))
#print('President #16 was', presidents['16'])
        
# for num, name in presidents.items(): 
  #  print('President number', num, 'was', name)


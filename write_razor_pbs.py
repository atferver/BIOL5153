#! /usr/bin/env python3

# say 'hello world'
#print('hello world')
# This script generates a PBS file for the AHPCC Razor cluster

#define some variables
queue = 'med16core'
wall = 1 #this is in hours

#This section prints the header/required info for the PBS script
print('#PBS -N assn4') # job name
print('#PBS -q' + ' ' + queue) #queue
print('#PBS -j oe') #STDOUT and STDERR into one file
print('#PBS -o assn4.$PBS_JOBID') #name of the output file
print('#PBS -l nodes=1:ppn=1') #how many resource to ask for (nodes = num nodes, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') #set the walltime (default to 1 hr)
print()

print('cd $PBS_O_WORKDIR')
print()

#load modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

#commands for this job
print('# insert commands here')
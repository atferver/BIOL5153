#!/bin/bash
  
#SBATCH -J Trinity-assembly
#SBATCH --partition comp06
#SBATCH -o Trinity_%j.txt
#SBATCH -e Trinity_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=atferver@uark.edu  
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --time=06:00:00

export OMP_NUM_THREADS=32
 
#load modules
module load samtools
module load jellyfish
module load bowtie2
module load salmon/0.8.2
module load java
 
#cd into directory youre submitting the script from
cd $SLURM_SUBMIT_DIR

#copy files from storage to scratch
rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID

#cd onto the scratch disk to run the job
cd /scratch/$SLURM_JOB_ID/

#run the Trinity assembly
/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2
 
#copy output files back to storage
rsync -av trinity_Run2 $SLURM_SUBMIT_DIR

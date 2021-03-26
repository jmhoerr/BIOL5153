#!/bin/bash/env python3

# SLURM script used for running jobs on the Pinnacle cluster

# define some variables
job = 'job_name'
queue = 'med16core'
name = 'jmhoerr_output_file'
node = 1
wall = 3 # this is in hours
  
print('#SBATCH --job-name=', job)
print('#SBATCH --q', queue)
print('#SBATCH --j oe') # join the STDOUT and STDERR into a single file
print('#SBATCH --o', name)
print('#SBATCH --partition comp72') 
print('#SBATCH --nodes=' + str(node))
print('#SBATCH --ntasks-per-node=32')
print('#SBATCH --time=0' + str(wall) + '6:00:00')

print('export OMP_NUM_THREADS=32')
 
print('# load required modules')
print('module load samtools')
print('module load jellyfish')
print('module load bowtie2')
print('module load salmon/0.8.2')
print('module load java')
 
print('# cd into the directory where you're submitting this script from')
print('cd $SLURM_SUBMIT_DIR')

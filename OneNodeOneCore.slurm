#!/bin/bash
#SBATCH --partition=snowy
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=0-02:00:00
#SBATCH --output=OneNodeOneCore.out
#SBATCH --error=ErrorOutput.err

# Load required modules
module purge
module load spartan_2019
module load foss/2019b
module load python/3.7.4

echo "Testing One Node One Core situation..........."
time srun -n 1 python3 test.py
echo "Completed!...................................."
#!/bin/bash
#SBATCH --account=b1094
#SBATCH --partition=ciera-himem
#SBATCH --constraint=quest10
#SBATCH --mem=50G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=7-00:00:00
#SBATCH --mail-user=michael.stroh@northwestern.edu
#SBATCH --mail-type=END
#SBATCH --job-name="ztf_dr14_source_list"

source /home/mcs8686/.bashrc

cd /projects/b1094/stroh/software/catalogs/ztf

conda activate py311

python create_source_catalog.py

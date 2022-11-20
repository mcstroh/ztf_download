#!/bin/bash
#SBATCH --account=b1094
#SBATCH --partition=ciera-himem
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=40GB
#SBATCH --time=14-00:00:00
#SBATCH --mail-user=michael.stroh@northwestern.edu
#SBATCH --mail-type=END
#SBATCH --job-name="ztf_dr14_download"

source /home/mcs8686/.bashrc

cd /projects/b1094/software/catalogs/ztf


wget -r -np -R "index.html*" -nH -e robots=off --no-parent --cut-dirs=3 https://irsa.ipac.caltech.edu/data/ZTF/lc_dr14

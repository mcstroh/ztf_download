#
# Scan over ZTF parquet files and create simple source catalog in csv format for db import
#
# Last modified: 2021-11-18 MCS
#

from glob import glob
import os
import pandas as pd
import subprocess
import sys



_ztf_directory = '/projects/b1094/stroh/software/catalogs/ztf/'
_data_release = 14

_ztf_dr_directory = f'{_ztf_directory}lc_dr{_data_release}/'
#_ztf_dr_db_directory = f'{_ztf_directory}db_dr{_data_release}'
_ztf_dr_db_directory = f'/scratch/mcs8686/db_dr{_data_release}'


def main():

    # Create a directory for the .csv files
    if not os.path.exists(_ztf_dr_db_directory):
        os.makedirs(_ztf_dr_db_directory)


    # Create a list of directories
    sub_dirs = sorted([x for x in glob(_ztf_dr_directory + '*') if os.path.isdir(x)])

    # First level directory structure
    for sub_dir in sub_dirs:
    
        print(sub_dir)
        
        # Grab field directories
        field_dirs = sorted([x for x in glob(sub_dir + '/*') if os.path.isdir(x)])
        for field_dir in field_dirs:
            print(field_dir)

            
            parquet_files = sorted([x for x in glob(field_dir + '/*.parquet') if os.path.isfile(x)])
            for parquet_file in parquet_files:
                print(parquet_file)
                
                csv_file_name = f"{_ztf_dr_db_directory}/{parquet_file.split('/')[-1].replace('parquet','csv.gz')}"
                
                df = pd.read_parquet(parquet_file)
                df['file_name'] = [parquet_file.split('/')[-1]] * df.shape[0]
                adjusted_df = df[['objectid','filterid','fieldid','rcid','objra','objdec','nepochs','file_name']].copy()
                adjusted_df.rename(columns={'objra':'ra','objdec':'decl'}, inplace=True)
                
                # Save to file
                adjusted_df.to_csv(csv_file_name, index=False, compression='gzip')
        


if __name__ == "__main__":
    main()

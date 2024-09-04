# idat2vcf (ACLI)

## Overview

This project automates the process of converting Illumina microarray .idat files to .vcf files using the array-analysis-cli tool. Additionally, it updates the gt_sample_summary.csv file with relevant information from a sample sheet automatically.

## Features:

    1. Selects manifest, cluster, and genome reference files for the analysis.
    2. Processes folders containing .idat files to generate genotype calls and convert .gtc files to .vcf.
    3. Updates gt_sample_summary.csv for each folder using the update_gt_sample_summary.py script.
    4. Runs all steps automatically for multiple folders.

## Installation

### Requirements

    1. Python 3.9+
    2. pandas
    3. ACLI (https://support-docs.illumina.com/ARR/ArrayAnalysisCLI/Content/ARR/IMA/Installation_Local.htm) 
    4. Other dependencies mentioned in your local environment (e.g., specific folders, files)

      Clone the repository:
      git clone https://github.com/yourusername/idat2vcf.git

      Install the required Python packages:
      pip install pandas
    
      Ensure that the array-analysis-cli (ACLI) is installed and accessible in your $PATH environment variable.

## Usage

    1. Place your manifest (.bpm, .csv, .egt) files and genome reference (.fa) file in the appropriate directories within your base directory.
    2. Add your .idat files to the respective subdirectories corresponding to sample IDs.
    
        /manifest/
           - *.bpm
           - *.egt
           - *.csv
       /ref/
           - *.fa
           - *.fai
       /folders_with_idat/
           - *.idat
       /output/
           - (output files will be saved here)

    3. Update the paths in the script as needed for your environment.

## Running the Script

To run the script, simply execute it with Python:
python3 your_script_name.py

## The script will:

    1. Automatically select the appropriate manifest, cluster, and reference genome files.
    2. Run genotype calling using array-analysis-cli.
    3. Convert the generated .gtc files into .vcf.
    4. Automatically update the gt_sample_summary.csv file using update_gt_sample_summary.py.

## Output

    1. .vcf files will be generated in the respective output subdirectories.
    2. The gt_sample_summary.csv will be updated with relevant sample information from the sample sheet for each folder.

## Script Breakdown

### Main Script (run_idat2vcf_acli.py)

The main script handles the process of running genotype calling, converting .gtc files to .vcf, and updating the gt_sample_summary.csv. The key steps are:

    1. Folder Processing: The script loops through each folder of .idat files.
    2. Genotype Calling: It runs the array-analysis-cli tool to generate genotype calls.
    3. GTC to VCF Conversion: Converts the .gtc files to .vcf format using the manifest and genome reference files.
    4. Updating the CSV: After processing each folder, the update_gt_sample_summary.py script is run to append new sample information to the summary CSV.

### Helper Script (update_gt_sample_summary.py)

This script updates the gt_sample_summary.csv by reading relevant information from the sample sheet corresponding to each folder. It appends the sample information to the existing summary CSV for a complete record.

### Shell script (run_idat2vcf_acli.sh)

This script is the shell script version of run_idat2vcf_acli.py. It should be run sequentially with update_gt_sample_summary.py

import os
import subprocess
import pandas as pd

# Define paths
base_dir = "/path/to/your/base/directory"
output_dir = os.path.join(base_dir, "output")

# Helper function to list files and get user input
def select_file(directory, extension):
    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    if not files:
        print(f"No files with extension {extension} found in {directory}")
        return None

    print(f"Available {extension} files:")
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")
    
    choice = int(input(f"Please enter the number of the {extension} file you want to use: ")) - 1
    return files[choice]

# Select manifest and cluster files
manifest_bpm = select_file(os.path.join(base_dir, "manifest"), ".bpm")
cluster_file = select_file(os.path.join(base_dir, "manifest"), ".egt")
manifest_csv = select_file(os.path.join(base_dir, "manifest"), ".csv")
genome_fasta = select_file(os.path.join(base_dir, "ref"), ".fa")

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List of folders with .idat files
folders = [
    "example_folder_1", "example_folder_2", "example_folder_3", 
    "example_folder_4", "example_folder_5"
    # Add more folder names as needed
]

# Function to run shell command and handle errors
def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

# Function to update gt_sample_summary.csv with sample sheet information
def update_gt_sample_summary(output_folder, folder):
    idat_folder = os.path.join(base_dir, folder)
    
    # Read the sample sheet CSV file
    sample_sheet_file = os.path.join(idat_folder, f"your_sample_sheet_prefix__{folder}_SampleSheet.csv")
    sample_sheet_df = pd.read_csv(sample_sheet_file, header=10, usecols=[0, 1, 2], nrows=8)
    
    # Read the gt_sample_summary.csv file
    gt_sample_summary_file = os.path.join(output_folder, "gt_sample_summary.csv")
    gt_sample_summary_df = pd.read_csv(gt_sample_summary_file)
    
    # Concatenate the two DataFrames horizontally
    updated_df = pd.concat([gt_sample_summary_df, sample_sheet_df], axis=1)
    
    # Write the updated DataFrame back to the CSV file
    updated_df.to_csv(gt_sample_summary_file, index=False)
    
    print(f"Updated {gt_sample_summary_file} with sample sheet information.")

# Loop through each folder and run the analysis
for folder in folders:
    idat_folder = os.path.join(base_dir, folder)
    output_folder = os.path.join(output_dir, folder)
    
    # Create output subdirectory for each folder
    os.makedirs(output_folder, exist_ok=True)
    
    # Run genotype calling
    command_call = (
        f"/path/to/your/array-analysis-cli/array-analysis-cli genotype call "
        f"--bpm-manifest {os.path.join(base_dir, 'manifest', manifest_bpm)} "
        f"--cluster-file {os.path.join(base_dir, 'manifest', cluster_file)} "
        f"--idat-folder {idat_folder} "
        f"--output-folder {output_folder}"
    )
    run_command(command_call)
    
    # Convert GTC to VCF with manifest matching
    command_vcf = (
        f"/path/to/your/array-analysis-cli/array-analysis-cli genotype gtc-to-vcf "
        f"--bpm-manifest {os.path.join(base_dir, 'manifest', manifest_bpm)} "
        f"--csv-manifest {os.path.join(base_dir, 'manifest', manifest_csv)} "
        f"--genome-fasta-file {os.path.join(base_dir, 'ref', genome_fasta)} "
        f"--gtc-folder {output_folder} "
        f"--output-folder {output_folder}"
    )
    run_command(command_vcf)
    
    # Update the gt_sample_summary.csv file with sample sheet information
    update_gt_sample_summary(output_folder, folder)

print("Analysis and update completed.")

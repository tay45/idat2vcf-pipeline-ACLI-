#!/bin/bash

# Define paths (Update these paths to match your directory structure)
base_dir="/path/to/base_directory"
output_dir="$base_dir/output"

# Select manifest and cluster files
echo "Available manifest files:"
ls "$base_dir/manifest"/*.bpm
read -p "Please enter the full name of the manifest BPM file you want to use: " manifest_bpm

echo "Available cluster files:"
ls "$base_dir/manifest"/*.egt
read -p "Please enter the full name of the cluster file you want to use: " cluster_file

echo "Available manifest CSV files:"
ls "$base_dir/manifest"/*.csv
read -p "Please enter the full name of the manifest CSV file you want to use: " manifest_csv

# Select reference genome file
echo "Available reference genome files:"
ls "$base_dir/ref"/*.fa
read -p "Please enter the full name of the reference genome file you want to use: " genome_fasta

# Create output directory if it doesn't exist
mkdir -p "$output_dir"

# List of folders with .idat files (You can modify this list or automate folder detection)
folders=(
    "folder_1" "folder_2" "folder_3" "folder_4" # Add or replace with your folder names
)

# Loop through each folder and run the analysis
for folder in "${folders[@]}"; do
    idat_folder="$base_dir/$folder"
    output_folder="$output_dir/$folder"
    
    # Create output subdirectory for each folder
    mkdir -p "$output_folder"
    
    # Run genotype calling
    /path/to/array-analysis-cli/array-analysis-cli genotype call \
        --bpm-manifest "$base_dir/manifest/$manifest_bpm" \
        --cluster-file "$base_dir/manifest/$cluster_file" \
        --idat-folder "$idat_folder" \
        --output-folder "$output_folder"
    
    # Convert GTC to VCF with manifest matching
    /path/to/array-analysis-cli/array-analysis-cli genotype gtc-to-vcf \
        --bpm-manifest "$base_dir/manifest/$manifest_bpm" \
        --csv-manifest "$base_dir/manifest/$manifest_csv" \
        --genome-fasta-file "$base_dir/ref/$genome_fasta" \
        --gtc-folder "$output_folder" \
        --output-folder "$output_folder"
done

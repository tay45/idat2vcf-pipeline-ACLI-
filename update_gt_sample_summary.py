import os
import pandas as pd

# Define paths
base_dir = "/path/to/base/directory"  # Example: path to the base directory where the data is located
output_dir = os.path.join(base_dir, "output")

# List of folders with .idat files
folders = [
    "folder1", "folder2", "folder3", "folder4", "folder5",
    "folder6", "folder7", "folder8", "folder9", "folder10",
    "folder11", "folder12", "folder13", "folder14", "folder15",
    "folder16", "folder17", "folder18", "folder19", "folder20",
    "folder21", "folder22", "folder23", "folder24", "folder25",
    "folder26", "folder27", "folder28", "folder29", "folder30",
    "folder31", "folder32"
]

# Function to update gt_sample_summary.csv
def update_gt_sample_summary():
    for folder in folders:
        idat_folder = os.path.join(base_dir, folder)
        output_folder = os.path.join(output_dir, folder)
        
        # Read the sample sheet CSV file
        sample_sheet_file = os.path.join(idat_folder, f"sample_sheet_{folder}.csv")  # Example: path to the sample sheet CSV
        sample_sheet_df = pd.read_csv(sample_sheet_file, header=10, usecols=[0, 1, 2], nrows=8)
        
        # Read the gt_sample_summary.csv file
        gt_sample_summary_file = os.path.join(output_folder, "gt_sample_summary.csv")
        gt_sample_summary_df = pd.read_csv(gt_sample_summary_file)
        
        # Concatenate the two DataFrames horizontally
        updated_df = pd.concat([gt_sample_summary_df, sample_sheet_df], axis=1)
        
        # Write the updated DataFrame back to the CSV file
        updated_df.to_csv(gt_sample_summary_file, index=False)
        
        print(f"Updated {gt_sample_summary_file} with sample sheet information.")

if __name__ == "__main__":
    update_gt_sample_summary()

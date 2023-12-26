#!/bin/bash

# Check if the correct number of arguments is given
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 input_directory [output_directory]"
    exit 1
fi

# Assign input and optional output directory from arguments
input_dir=$1
output_dir=${2:-"output_dir"}

# Create the output directory if it doesn't exist
if [ ! -d "$output_dir" ]; then
  mkdir -p "$output_dir"
fi

# Function to process a file
process_file() {
    file=$1
    output_dir=$2
    basefilename=$(basename "$file")
    python3 to_csv.py -m "$file" -c "${output_dir}/${basefilename}.csv"
}

# Export the function to be used by parallel
export -f process_file

# Find all .mid files and use GNU Parallel to process them
find "$input_dir" -maxdepth 1 -name '*.mid' | parallel -j 7 process_file {} "$output_dir"


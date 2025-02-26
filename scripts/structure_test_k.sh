#!/bin/bash

# structure binary and mainparams and extraparams files should be in
# the same directory as this script

# Function to display usage information
usage() {
    echo "Usage: $0 -i <input_file> -o <output_directory> -k <value_k> -r <value_r>"
    exit 1
}

# Parse named parameters using getopts
while getopts ":i:o:k:r:" opt; do
    case "${opt}" in
        i)
            input_file=${OPTARG}
            ;;
        o)
            output_dir=${OPTARG}
            ;;
        k)
            value_k=${OPTARG}
            ;;
        r)
            value_r=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND - 1))

# Validate that all parameters were provided
if [ -z "${input_file}" ] || [ -z "${output_dir}" ] || [ -z "${value_k}" ] || [ -z "${value_r}" ]; then
    usage
fi

# Create the output directory if it doesn't exist
mkdir -p "${output_dir}"

for (( k = 1; k <= value_k; k++ ))
do
    for (( r = 1; r <= value_r; r++ ))
    do
        ./structure -i "${input_file}" -o "${output_dir}/k${k}_${r}" -K "${k}" -m mainparams -e extraparams
    done
done
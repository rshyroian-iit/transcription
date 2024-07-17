#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: transcribe <input_file>"
    exit 1
fi

input_file=$1

# Run the Python script
python3 transcribe.py "$input_file"


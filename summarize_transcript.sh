#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: summarize_transcript <transcript_file>"
    exit 1
fi

transcript_file=$1

# Run the Python script
python3 summarize_transcript.py "$transcript_file"

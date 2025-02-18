#!/bin/bash

# Define folder paths
FOLDER_A="$1"
FOLDER_B="$2"

# Loop through all .WAV files in Folder A
for wav_file in "$FOLDER_A"/*.wav; do
    # Extract the filename without extension
    filename=$(basename "$wav_file" .wav)
    	
    echo $wav_file

    # Check if the corresponding .TextGrid file exists in Folder B
    if [ -f "$FOLDER_B/$filename.TextGrid" ]; then
        # Copy the matching file to Folder A
        cp "$FOLDER_B/$filename.TextGrid" "$FOLDER_A/"
    fi
done

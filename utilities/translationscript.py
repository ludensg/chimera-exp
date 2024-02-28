import os
import re

# Function to check if a line contains Chinese characters
def contains_chinese(line):
    return any('\u4e00' <= char <= '\u9fff' for char in line)

# Function to process each file
def process_file(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if contains_chinese(line):
                output_file.write(f"{file_path}:{i+1}: {line}")

# Function to walk through directories, skipping specified ones
def walk_and_process(start_dir, output_path, skip_dirs):
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk(start_dir):
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in skip_dirs]  # Skip specified directories
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    process_file(file_path, output_file)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

# Define the start directory and output file path
start_dir = '.'  # Current directory
output_path = 'chinese_characters_lines.txt'

# Directories to skip
skip_dirs = [os.path.join('.', 'chimera-env'), os.path.join('.', 'Chimera', 'bert_data')]

# Run the script
walk_and_process(start_dir, output_path, skip_dirs)

print(f"Processing complete. Output saved to {output_path}")

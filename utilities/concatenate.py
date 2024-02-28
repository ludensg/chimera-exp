import os

# Define the output file name
output_file_name = 'concatenated_code_files.txt'

# Define the types of files to include, e.g., Python files only
included_extensions = ['.py', '.sh']

# Open the output file in write mode
with open(output_file_name, 'w') as output_file:
    # Iterate over each item in the current directory
    for item in os.listdir('.'):
        # Check if the item is a file and has an included extension
        if os.path.isfile(item) and any(item.endswith(ext) for ext in included_extensions):
            # Write a header for the file
            output_file.write(f'===== {item} =====\n\n')
            # Open and read the current file
            with open(item, 'r') as input_file:
                # Write the content of the file to the output file
                output_file.write(input_file.read())
                # Add a newline after the content for separation
                output_file.write('\n\n')

print(f"All code files have been concatenated into {output_file_name}.")

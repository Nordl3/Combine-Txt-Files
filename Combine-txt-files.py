import os

def combine_txt_files_in_current_folder():
    # Get the current working directory (where the script is located)
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # Set the output file path in the same folder
    output_file = os.path.join(current_folder, 'combined_code.txt')
    
    # Open the output file for writing
    with open(output_file, 'w') as outfile:
        # Loop through all files in the current folder
        for filename in os.listdir(current_folder):
            if filename.endswith(".txt"):
                file_path = os.path.join(current_folder, filename)
                
                # Open each file and write its contents to the output file
                with open(file_path, 'r') as infile:
                    outfile.write(infile.read())
                
                # Add a blank line between files
                outfile.write("\n\n")

    print(f"All .txt files have been combined into {output_file}.")

# Call the function to combine the files when the script is run
if __name__ == "__main__":
    combine_txt_files_in_current_folder()

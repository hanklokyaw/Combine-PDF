from PyPDF2 import PdfMerger
import os

def combine_pdfs(input_dir, output_file):
    merger = PdfMerger()

    # export as pdf
    output_file = input_dir + '/' + output_file + ".pdf"

    # Get list of PDF files in input directory
    pdf_files = [file for file in os.listdir(input_dir) if file.endswith('.pdf')]

    # Sort PDF files alphabetically
    pdf_files.sort()

    # Iterate over PDF files and append them to the merger
    for pdf_file in pdf_files:
        with open(os.path.join(input_dir, pdf_file), 'rb') as file:
            merger.append(file)

    # Write merged PDF to output file
    with open(output_file, 'wb') as output:
        merger.write(output)

    print("PDFs combined successfully!")


def get_filepath():
    # Get the file path from the user
    filepath = input(f'Enter your filepath: ')
    print(filepath)
    output_filename = input(f'Enter the file name that you want to save: ')

    # Remove surrounding quotes if present
    if filepath.startswith('"') and filepath.endswith('"'):
        filepath = filepath[1:-1]

    # Replace backslashes with forward slashes
    filepath = filepath.replace('\\', '/')

    return filepath, output_filename


# Example usage:
# input_directory = "C:/Users/hank.aungkyaw/Downloads/pdf_combine"
# output_file = "C:/Users/hank.aungkyaw/Downloads/pdf_combine/combined_file.pdf"

input_directory, target_filename = get_filepath()
combine_pdfs(input_directory, target_filename)

# PDF Merger Tool

## Description

The PDF Merger Tool is a Python script designed to merge multiple PDF files within a specified directory into a single PDF file. This tool is useful for combining multiple documents into one, making it easier to manage and share.

## Features

- Merges all PDF files in a given directory into a single PDF.
- Automatically processes files with the `.pdf` extension.
- Outputs a single, combined PDF file.

## Requirements

- Python 3.x
- `PyPDF2` library (Install using `pip install PyPDF2`)

## How It Works

1. **Initialize PdfMerger**: The script starts by initializing a `PdfMerger` object from the `PyPDF2` library.
2. **Change Directory**: It changes the working directory to the specified directory containing the PDF files.
3. **Iterate Over Files**: The script iterates through each file in the directory, checking if it has a `.pdf` extension.
4. **Append to Merger**: Each PDF file is appended to the merger object.
5. **Write Merged PDF**: The merged PDF is written to the specified output file.

## How to Run

1. **Install `PyPDF2`**: First, ensure you have the `PyPDF2` library installed:

    ```bash
    pip install PyPDF2
    ```

2. **Clone or Download**: Clone or download this repository to your local machine.

3. **Open Terminal or Command Prompt**: Open a terminal or command prompt.

4. **Navigate to the Directory**: Navigate to the directory where the script is located.

5. **Run the Script**: Run the script using Python:

    ```bash
    python Merge_Pdf_File.py
    Enter the Dir path
    Enter the output file name .pdf
    ```



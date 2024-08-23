import os 
from PyPDF2 import PdfMerger

def merge_pdf(path, output_file):

    merger = PdfMerger()

    os.chdir(path)

    for filename in os.listdir(path):

        if filename.endswith('.pdf'):

            merger.append(filename)

    with open(output_file, 'wb') as outfile:
        merger.write(outfile)

    merger.close()

    print(f"All Pdf Have Ben Merged Into {output_file}")

path = input("Enter your path : ")
output_file = input("Enter your output file name : ")
merge_pdf(path, output_file)


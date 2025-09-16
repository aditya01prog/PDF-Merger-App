from PyPDF2 import PdfWriter

merger = PdfWriter()

PDFs = []
n = int(input("How many PDFs you want to merge ? \n"))

for i in range(0, n):
    name = input(f"Enter the name of pdf {i+1}: ")
    PDFs.append(name)

for pdf in PDFs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
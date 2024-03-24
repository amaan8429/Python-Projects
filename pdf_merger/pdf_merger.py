import PyPDF2
import sys
import os

path = "C:/Users/amaan/Downloads/PDF-MERGER"
finalpath = "C:/Users/amaan/Downloads/PDF-MERGER/final"
os.mkdir(finalpath)

with os.scandir(path) as pdfs:
    merger = PyPDF2.PdfMerger()
    for pdf in pdfs:
        
        if pdf.name.endswith(".pdf"):
            with open (pdf,'rb') as p:
                merger.append(p)
                p.close()

    merger.write("merged.pdf")
    print("all done")
    merger.close()



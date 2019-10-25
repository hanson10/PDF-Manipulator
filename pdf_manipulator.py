# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os

'''
prefix = "S:\\Scans\\photo album\\"
pdf_files = ["0-5.pdf", "6-10.pdf", "11-16.pdf", 
             "17-27.pdf", "28.pdf", "29-40.pdf", 
             "41-62.pdf", "63-86.pdf", "87-100.pdf",
             "101-120.pdf", "121-131.pdf"]
'''

def pdfMerge(prefix, filenames, out_file):
    merger = PdfFileMerger()
    for filename in filenames:
        merger.append(prefix + filename)
    merger.write(out_file + ".pdf")
    merger.close()

# -----------------------------------------
'''
photo_album = "C:\\Users\\Jack\\Documents\\photo-album.pdf"
''' 

def pdfBreaker(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        
        output_filename = "{}_page_{}".format(fname, page+1)
        with open(output_filename, "wb") as out:
            pdf_writer.write(out)
            

# -------------------------------------------------
            
from pdf2image import convert_from_path

from pdf2image.exceptions import (
        PDFInfoNotInstalledError,
        PDFPageCountError,
        PDFSyntaxError
    )

def pdf_to_png(path, file_basename):
    images = convert_from_path(path)
    for i, image in enumerate(images):
        fname = file_basename + str(i) + ".png"
        image.save(fname, "PNG")
        print(fname + " saved")
    
    
    
    
    
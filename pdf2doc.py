#!/usr/bin/env python 

#pip install aspose.words
import aspose.words as aw

#load the PDF document from your disc drive (C://Users/USER/document.pdf.....Make sure the PDf document is in this (C://Users/USER/ PATH)
doc = aw.Document("filename.pdf") #name of the PDF file here

#save the document to DOCX format
doc.save("filename.docx") #put any name of the docx u want it to save as


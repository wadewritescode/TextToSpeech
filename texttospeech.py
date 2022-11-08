from gtts import gTTS
import os
import PyPDF2

pdf = input(r"""Paste the link to the pdf... 
""")


# creating a pdf file object
pdfFileObj = open(pdf, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())


mytext = pageObj.extractText()
audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("example.mp3")
os.system("start example.mp3")


# closing the pdf file object
pdfFileObj.close()

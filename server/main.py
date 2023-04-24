


import streamlit as st
import PyPDF2
import os 
from PIL import Image
import pytesseract
from PIL import Image
BG = Image.open("myfont/bg.png")
sizeOfSheet =BG.width
gap, _  = 0,0
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'
def writee(char):
    global gap, _
    if char == '\n':
        pass
    else:
        char.lower()
        cases = Image.open("myfont/%s.png"%char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases

def letterwrite(word):
    global gap, _
    if gap > sizeOfSheet - 95*(len(word)):
        gap = 0
        _ += 200
    for letter in word:        
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'            
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketcl'
            elif letter == '-':
                letter = 'hiphen'
            writee(letter)
def worddd(Input):
    wordlist=Input.split(' ')
    for i in wordlist:
        letterwrite(i)
        writee('space')

def pdfToText(path):
    pdfreader = PyPDF2.PdfFileReader(path)
    no_of_pages = pdfreader.numPages
    with open('final_txt.txt', 'w') as f:
        for i in range(0, no_of_pages):
            pagObj = pdfreader.getPage(i)
            f.write(pagObj.extractText())
    with open('final_txt.txt', 'r') as f:
        text = f.read()
    if os.path.exists("final_txt.txt"):
        pass
        return text


from fpdf import FPDF
from PIL import Image

imagelist=[]
for i in range(0,len(p)):
    imagelist.append('%doutt.png'%i)

#Converting images to pdf
#Source:https://datatofish.com/images-to-pdf-python/


def pdf_creation(PNG_FILE,flag=False):
    rgba = Image.open(PNG_FILE)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
    rgb.paste(rgba, mask=rgba.split()[3])               # paste using alpha channel as mask
    rgb.save('final_output.pdf', append=flag)  #Now save multiple images in same pdf file

#First create a pdf file if not created
pdf_creation(imagelist.pop(0))

#Now I am opening each images and converting them to pdf 
#Appending them to pdfs
for PNG_FILE in imagelist:
    pdf_creation(PNG_FILE,flag=True)

st.title("document to handwritting convertor")
st.write("upload your document and get it converted to handwritting")


style_name = st.sidebar.selectbox(
    'Select HandWriting',
    ("Style-1", "Style-2", "Style-3", "Style-4", "Style-5")
)


if __name__ == '__main__':
    file = st.file_uploader("upload your document", type=["pdf", "docx", "txt","png","jpg","jpeg"])

    if file is not None:
        try:
            with open('sample.txt', 'r') as file:
                data = file.read().replace('\n', '')
            l=len(data)
            nn=len(data)//600
            chunks, chunk_size = len(data), len(data)//(nn+1)
            p=[ data[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
            
            for i in range(0,len(p)):
                worddd(p[i])
                writee('\n')
                BG.save('%doutt.png'%i)
                BG1= Image.open("myfont/bg.png")
                BG=BG1
                gap = 0
                _ =0
        except ValueError as E:
            print("{}\nTry again".format(E))


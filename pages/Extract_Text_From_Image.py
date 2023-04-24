import os
import sys

import pytesseract
from PIL import Image
import streamlit as st

# You must specify the full path to the tesseract executable.
# In Linux, you can get this by using the command:
# which tesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# add windows path here if you are using windows and comment the above line
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def main():
    st.title("lazylearn(Text Extracter From Image)")
    
    uploaded_file = st.file_uploader("Upload your images:", type=["png", "jpg", "jpeg", "gif"])
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.write('Selected Image is')
        st.image(img, caption=f"Image {uploaded_file.name}")
        ocrText = pytesseract.image_to_string(img, timeout=5)
        # st.write("OCR Result:", ocrText)
        st.write("")

        # Add a button to download the OCR result as a text file
        text_file = open(f"{uploaded_file.name}.txt", "w")
        text_file.write(ocrText)
        text_file.close()
        st.download_button(label="Download as Text file", data=ocrText, file_name=f"{uploaded_file.name}.txt", mime="text/plain")
    

if __name__ == "__main__":
    main()

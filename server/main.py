
import uuid
import datetime
import streamlit as st
import os 


def get_user_id():
    user_id = st.secrets["user_id"]
    return user_id

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
        os.remove("final_txt.txt")
        return text

def convert_pdf_to_handwriting(file):
    user_id = get_user_id()
    file_name = file.name
    file_type = file.type
    file_id = str(uuid.uuid4())
    file_path = f"uploads/{file_id}.{file_type}"
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path


st.title("document to handwritting convertor")
st.write("upload your document and get it converted to handwritting")

file = st.file_uploader("upload your document", type=["pdf", "docx", "txt","png","jpg","jpeg"])

if file is not None:
    # print file details
    st.write("file name: ", file.name)
    st.write("file type: ", file.type)

    # convert file to handwriting
    convert_button = st.button("convert")
    if convert_button:
        file_path = convert_pdf_to_handwriting(file)
        st.write("file converted successfully")
        st.write("file path: ", file_path)

        # download converted file
        download_button = st.button("download")
        if download_button:
            st.markdown(f"[download file]({file_path})")


    
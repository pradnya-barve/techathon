
# import uuid
# import datetime
# import streamlit as st
# import os 
# import pywhatkit as pwk


# # def get_user_id():
# #     user_id = st.secrets["user_id"]
# #     return user_id




# # def textToHandWritten(text):
# #     user_id = get_user_id()
# #     file_name = f"{user_id}_{str(uuid.uuid4())}_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
# #     file_path = f"downloads/{file_name}.png"
# #     pwk.text_to_handwriting(text, output_file=file_path)
# #     st.write(file_path)
# #     return file_path

# # def docxToText(path):
# #     pass 
# #     # doc = docx.Document(path)
# #     # fullText = []
# #     # for para in doc.paragraphs:
# #     #     fullText.append(para.text)
# #     # return '\n'.join(fullText)

# # def imageToHandWritten(path):
# #     user_id = get_user_id()
# #     file_name = f"{user_id}_{str(uuid.uuid4())}_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
# #     file_path = f"downloads/{file_name}.png"
# #     pwk.image_to_ascii_art(path, output_file=file_path)
# #     return file_path


# # def convert(file):
# #     if file.type == "application/pdf":
# #         text = pdfToText(file)
# #         file_path = textToHandWritten(text)
# #     elif file.type == "text/plain":
# #         text = file.read().decode("utf-8")
# #         file_path = textToHandWritten(text)
# #     elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
# #         text = docxToText(file)
# #         file_path = textToHandWritten(text)
# #     elif file.type == "image/png" or file.type == "image/jpeg":
# #         file_path = imageToHandWritten(file)
# #     return file_path

# st.title("document to handwritting convertor")
# st.write("upload your document and get it converted to handwritting")

# file = st.file_uploader("upload your document", type=["pdf", "docx", "txt","png","jpg","jpeg"])


# # if file is not None:
# #     # print file details
# #     st.write("file name: ", file.name)
# #     st.write("file type: ", file.type)

# #     # convert file to handwriting
# #     convert_button = st.button("convert")
# #     if convert_button:
# #         file_path = convert(file)
# #         st.write("your file is ready")
# #         st.image(file_path)


import streamlit as st
import PyPDF2
import os 

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



st.title("document to handwritting convertor")
st.write("upload your document and get it converted to handwritting")

file = st.file_uploader("upload your document", type=["pdf", "docx", "txt","png","jpg","jpeg"])

if file is not None:
    # print file details
    if file.type == "application/pdf":
        st.write("file name: ", file.name)
        st.write("file type: ", file.type)

        # convert file to handwriting
        convert_button = st.button("convert")
        if convert_button:
            file_content = pdfToText(file)
            st.write("file_content: ", file_content)
        
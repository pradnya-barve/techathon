import streamlit as st
from PIL import Image
import os
import imghdr
from io import BytesIO
import base64
import tempfile
from PdffromImage import do_work
import PdffromImage as dt
import docx2txt
from PIL import ImageFile
import PyPDF2
ImageFile.LOAD_TRUNCATED_IMAGES = True
import time



# @st.cache_data
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

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    return f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}"><input type="button" style="background-color:#fa5f2f; color:white" value="DOWNLOAD"></a>'

main_bg = "./images/t3.jpg"

main_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("WriteMate - Text to Handwriting")

# creating a side bar for picking the style of image
style_name = st.sidebar.selectbox(
    'Select HandWriting',
    ("Normal", "Clean", "Normal-with-italic", "Messy", "Bold")
)

page_type = st.sidebar.selectbox(
    'Select Page Type',
    ("A4", "A5", "A6")
)

ink_color = st.sidebar.selectbox(
    'Select Ink Color',
    ("Black", "Blue", "Green", "Red")
)

page_margin = st.sidebar.selectbox(
    'Select Page Margin',
    ("Small", "Medium", "Large")
)

if page_margin is not None:
    if page_margin == "Small":
        dt.margin = '115'
    elif page_margin == "Medium":
        dt.margin = '150'
    elif page_margin == "Large":
        dt.margin = '200'
    else:
        dt.margin = '115'

wordsPerLine = st.sidebar.selectbox(
    'Select Words Per Line',
    ("Small(60)", "Medium(75)", "Large(90)")
)


lineGap = st.sidebar.slider('Select Line Gap', 0, 200, 120)

root_style = "./images/"
path_style = os.path.join(root_style, style_name+".jpg")
root_font = "./Fonts/"

# Upload text file functionality
img = None
uploaded_file = st.file_uploader(
    "Choose a text file...", type=["txt", "docx", "pdf"])

show_file = st.empty()

# checking if user has uploaded any file
if not uploaded_file:
    show_file.info(
        "Please Upload the text/docx/pdf document (no .doc only .docx and .txt) ")


if uploaded_file is not None:
    ###########################
    # file_details = {"Filename": uploaded_file.name,
    #                 "FileType": uploaded_file.type}
    # st.write(file_details)

    if uploaded_file.type == "text/plain":
        raw_text = str(uploaded_file.read(), "utf-8")

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":

        raw_text = docx2txt.process(uploaded_file)
    
    elif uploaded_file.type == "application/pdf":
        raw_text = pdfToText(uploaded_file)

    ###########################

    size = f' Input File Size in MegaBytes is {"{0:.4f}".format(uploaded_file.size / (1024 * 1024))}'
    st.markdown("%s" % size,
                unsafe_allow_html=True)
    try:
        name, _ = uploaded_file.name.split('.')
    except:
        st.error("File Name is Not Valid")

    convert_button = st.button("Convert")

    

    # user presses convert
    if convert_button:

        processing_text = st.subheader("Processing...")

        # progress_text = "Processing..."
        my_bar = st.progress(0, text='')

        for percent_complete in range(50):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1, text='')

        
        lines = raw_text.split("\n")  # splitting text on the basis of new line

        dt.background = Image.open("./images/a4.jpg")

        dt.SheetWidth = dt.background.width
        dt.SheetHieght = dt.background.height

        dt.margin = 115
        dt.lineMargin = 115
        dt.allowedCharacters = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ
                                abcdefghijklmnopqrstuvwxyz
                                #:,.?-!()[]'<>=%^$@_;1234567890 "'''

        dt.wordsPerLine = 75
        dt.maxLenPerPage = 3349
        dt.pageNum = 1


        dt.FontType = os.path.join(root_font, style_name)

        dt.lineGap = 120
        dt.writing = style_name

        
        # Initializing x and y
        dt.x, dt.y = dt.margin + 20, dt.margin + dt.lineGap

        # Asking for the quality of the output
        dt.scale_percent = 30
        dt.images_list = []

        final_image = do_work(lines, name)

        path = name + '_' + style_name + '_output.pdf'

        with tempfile.TemporaryDirectory() as tmpdirname:

            final_path = os.path.join(tmpdirname, path)
            final_image.save(final_path)

            file_stats = os.stat(final_path)

            size_file = file_stats.st_size / (1024 * 1024)

            s = f'Output File Size in MegaBytes is {"{0:.2f}".format(size_file)}'
            st.markdown("%s" % s,
                        unsafe_allow_html=True)
            if processing_text:
                processing_text.empty()
                my_bar.empty()
            processing_text.subheader("File is ready! Click below to download")

            st.markdown(get_binary_file_downloader_html(
                final_path, file_label='File'), unsafe_allow_html=True)


    # displaying the image
    st.subheader("Chosen Handwriting is")

    st.image(path_style, caption='Chosen Handwriting', use_column_width=True)
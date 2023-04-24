
from server.db import client
import uuid
import datetime
import streamlit as st


def get_user_id():
    user_id = st.secrets["user_id"]
    return user_id


st.title("document to handwritting convertor")
st.write("upload your document and get it converted to handwritting")

file = st.file_uploader("upload your document", type=["pdf", "docx", "txt","png","jpg","jpeg"])

if file is not None:
    # print file details
    st.write("file name: ", file.name)
    st.write("file type: ", file.type)

    
import streamlit as st
from PIL import Image
import pytesseract
import tempfile
import os
import pdf2image
import docx2txt

st.title("Text Extractor")
st.write("Upload an image, PDF, or Word document and extract text from it.")

uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg", "pdf", "docx"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()

    if file_extension in ["png", "jpg", "jpeg"]:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        extracted_text = pytesseract.image_to_string(img)
        st.header("Extracted Text")
        st.code(extracted_text)

    elif file_extension == "pdf":
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name
            temp_file.write(uploaded_file.getbuffer())

        images = pdf2image.convert_from_path(temp_filename)

        extracted_text = ""
        for image in images:
            st.image(image, caption="Extracted Image", use_column_width=True)
            img_gray = image.convert("L")
            text = pytesseract.image_to_string(img_gray)
            extracted_text += text + "\n"
        st.header("Extracted Text")
        st.code(extracted_text)
        os.remove(temp_filename)

    elif file_extension == "docx":
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name
            temp_file.write(uploaded_file.getbuffer())
        extracted_text = docx2txt.process(temp_filename)
        st.header("Extracted Text")
        st.code(extracted_text)
        os.remove(temp_filename)

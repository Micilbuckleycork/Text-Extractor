import streamlit as st
from PIL import Image
import pytesseract

# Set up Streamlit app title and description
st.title("Image Text Extractor")
st.write("Upload an image and extract text from it.")

# Display file uploader
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Load the image
    img = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    # Perform OCR and extract text from the image
    extracted_text = pytesseract.image_to_string(img)
    
    # Display the extracted text
    st.header("Extracted Text")
    st.code(extracted_text)

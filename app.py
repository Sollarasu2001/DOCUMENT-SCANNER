import streamlit as st
from document_scanner import process_image

st.title("DOCUMENT SCANNER")

#upload image file
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    #Process Image
    image_bytes = uploaded_file.getbuffer()
    text = process_image(image_bytes)

    #Display extracted text
    st.header("EXTRACTED TEXT")
    st.write(text)

    #Save text to file
    @st.cache
    def convert_df(text):
        return text
    
    df = convert_df(text)

    st.download_button(
        label = "Save Text",
        data = df,
        file_name = "extracted_text.txt",
        mime = "text/plain"
    )
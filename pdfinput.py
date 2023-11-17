import streamlit as st
from extract_text import PDFTextExtractor


def app():
    # Sidebar: File uploader for PDF
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    st.info("Please Upload the 20 to 30 pages Pdf only")
    if pdf_file is not None and st.button("Submit"):
        # Instantiate PDFTextExtractor class with BytesIO object
        pdf_extractor = PDFTextExtractor(pdf_file)

        # Extract text from PDF
        extracted_text = pdf_extractor.extract_text_from_pdf()

        # Save the extracted text to a text file with the same base name
        pdf_extractor.save_text_to_file(extracted_text)

        st.success("Text is Extracted, Now you can use the ChatBot")


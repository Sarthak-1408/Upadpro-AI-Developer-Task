import os
import PyPDF2
from io import BytesIO

class PDFTextExtractor:
    def __init__(self, pdf_source):
        if isinstance(pdf_source, str):
            self.pdf_path = pdf_source
            self.file_object = None
        elif isinstance(pdf_source, BytesIO):
            self.pdf_path = None
            self.file_object = pdf_source
        else:
            raise ValueError("Unsupported PDF source. Use either file path or BytesIO object.")

    def extract_text_from_pdf(self):
        text = ""
        try:
            if self.pdf_path:
                with open(self.pdf_path, "rb") as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    num_pages = len(pdf_reader.pages)

                    for page_num in range(num_pages):
                        page = pdf_reader.pages[page_num]
                        text += page.extract_text()
            elif self.file_object:
                pdf_reader = PyPDF2.PdfReader(self.file_object)
                num_pages = len(pdf_reader.pages)

                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()

        except Exception as e:
            print(f"An error occurred: {e}")

        return text

    def save_text_to_file(self, text):
        # Extract the base name without path and extension
        pdf_name = os.path.splitext(os.path.basename(self.pdf_path))[0] if self.pdf_path else "extracted_data"

        # Save the extracted text to a text file with the same base name
        txt_path = f"Knowledge/{pdf_name}.txt"

        try:
            # Create "Knowledge" folder if it doesn't exist
            knowledge_folder = "Knowledge"
            if not os.path.exists(knowledge_folder):
                os.makedirs(knowledge_folder)
                print(f"Created '{knowledge_folder}' folder.")
            else:
                print(f"'{knowledge_folder}' folder already exists.")

            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
            print(f"Extracted text saved to: {txt_path}")
        except Exception as e:
            print(f"An error occurred while saving the text: {e}")

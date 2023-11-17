# Upadpro Software & Services Pvt. Ltd.
## AI/ML Developer Task - ChatBot
This repository contains the code for an interactive chatbot application that allows users to upload PDF files, extract text from PDFs, parse text from URLs, and engage in a chat conversation with the chatbot. This task is provided by Upadpro Software & Services Pvt. Ltd.

## Demo Video
https://github.com/Sarthak-1408/SunBase-Assignment-Solution/assets/72247049/03dbf3f4-e0a2-4fd3-a1e6-52d1bf84867f

## Features

- **PDF Text Extraction**: Users can upload PDF files, and the application extracts text from the uploaded PDF using PyPDF2.

- **URL Text Parsing**: Users can input a URL, and the application parses the text content from the provided URL using BeautifulSoup.

- **Chatbot Integration**: The application incorporates a chatbot powered by LlamaIndex. Users can interact with the chatbot and ask questions related to the extracted text.

- **Multi-App Structure**: The project is organized using a multi-app structure, allowing users to choose between different functionalities (PDF, URL, ChatBot) using Streamlit.

## Folder Structure

- **extract_text.py**: Contains the `PDFTextExtractor` class responsible for extracting text from PDFs and saving it to a text file.

- **chatbot.py**: Implements the chatbot functionality using LlamaIndex and Streamlit's chat components.

- **pdfinput.py**: Defines the Streamlit app for handling PDF file uploads, text extraction, and interaction with the chatbot.

- **urlinput.py**: Implements the Streamlit app for URL input, text extraction from URLs, and interaction with the chatbot.

- **app.py**: Orchestrates the multi-app structure, allowing users to choose between PDF, URL, and ChatBot functionalities.

## Instructions

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    streamlit run app.py
    ```

4. Open your web browser and navigate to the provided local URL.

## Dependencies

- streamlit
- PyPDF2
- beautifulsoup4
- llama_index

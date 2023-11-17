import streamlit as st
import requests
from bs4 import BeautifulSoup
import os

def app():
    st.title("URL Text Extractor")

    # Sidebar: Text input for URL
    url = st.text_input("Enter URL")

    if st.button("Extract Text"):
        # Validate that a URL is provided
        if not url:
            st.warning("Please enter a valid URL.")
        else:
            try:
                # Make a request to the URL
                response = requests.get(url)
                response.raise_for_status()  # Check if the request was successful

                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract text from the parsed HTML
                parsed_text = soup.get_text()

                # Save the parsed text to a text file in the Knowledge folder
                if parsed_text:
                    # Extract the base name without path and extension from the URL
                    url_base_name = os.path.splitext(os.path.basename(url))[0]

                    # Save the parsed text to a text file with the same base name
                    txt_path = f"Knowledge/{url_base_name}_parsed.txt"

                    with open(txt_path, 'w', encoding='utf-8') as txt_file:
                        txt_file.write(parsed_text)
                    
                    st.success("Text is Extracted, Now you can use the ChatBot")

            except Exception as e:
                st.error(f"An error occurred: {e}")

# Sample Data
# https://towardsdatascience.com/type-hinting-dataframes-for-static-analysis-and-runtime-validation-3dedd2df481d
# https://towardsdatascience.com/tsmixer-the-latest-forecasting-model-by-google-2fd1e29a8ccb

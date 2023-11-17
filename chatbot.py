from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
import streamlit as st
import openai

openai.api_key = "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"

def app():
    st.title("Upadpro AI/ML Developer Task, ChatBot")
    st.header("Chat with the uploaded Document, powered by LlamaIndex 💬🦙")
            
    if "messages" not in st.session_state.keys(): # Initialize the chat messages history
        st.session_state.messages = [
            {"role": "assistant", "content": "Ask me a question!"}
        ]

    @st.cache_resource(show_spinner=False)
    def load_data():
        with st.spinner(text="Loading and indexing the document – hang tight! This should take 1-2 minutes."):
            reader = SimpleDirectoryReader(input_dir="Knowledge", recursive=True)
            docs = reader.load_data()
            service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the Streamlit Python library and your job is to answer technical questions. Assume that all questions are related to the Streamlit Python library. Keep your answers technical and based on facts – do not hallucinate features."))
            index = VectorStoreIndex.from_documents(docs, service_context=service_context)
            return index
        
    index = load_data()

    if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
            st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

    if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages: # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message) # Add response to message histor
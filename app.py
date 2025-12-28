#importing required libraries
import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client with API key from environment
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def retriever_info(query):
    # Dummy implementation for example purposes
    return 

def rag_query(query):
    retrieved_info = retriever_info(query)
    augmented_prompt = f"User query: {query}. Retrieved information: {retrieved_info}"
    
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Recommended Groq model [web:1][web:17]
        messages=[{"role": "user", "content": augmented_prompt}],
        max_tokens=300,
        temperature=0.2,
        top_p=1.0,
        frequency_penalty=0.1,
        presence_penalty=0.0
    )
    
    return chat_completion.choices[0].message.content.strip()  # Updated response path [web:1]

# Streamlit UI
st.title("RAG Prompt Query Interface (Groq API)")
user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    if user_input:
        with st.spinner("Generating response..."):
            response = rag_query(user_input)
            st.success("Response:")
            st.write(response)
    else:
        st.warning("Please enter a query.")



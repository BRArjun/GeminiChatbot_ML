#Import necessary libraries
import streamlit as st
import os
import google.generativeai as genai
import time

#Setting the page and tab titles 
st.set_page_config(page_title="Gemini Chatbot")
st.title("_:blue[Gemini]_ Chatbot Clone")

# Configure Generative AI API key
genai.configure(api_key='YOUR_API_KEY')

# Function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to get response from Gemini
def get_gemini_response(question):
    try:
        response = model.generate_content(question, stream=True)
        return response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

#Give the prompt to the model
if prompt := st.chat_input("Your Query"):

    # Get Gemini response
    response = get_gemini_response(prompt)

    # Add user query and response to chat history
    st.session_state['chat_history'].append(("You", prompt))
    
    #Response Styling
    st.subheader("_:blue[Response]_")
    
    #A string to hold the response string given by the model
    full_response=""
    
    #Initialize empty placeholder for displaying
    t=st.empty()
    
    #Iterate through the response of the model
    for chunk in response:
        for char in chunk.text:
            if char==' ':
                full_response+=char
                t.write(full_response)
                time.sleep(0.1)
            else:
                full_response+=char
                t.write(full_response)
                time.sleep(0.1)
    
    #Add the response text to chat history to be seen
    st.session_state['chat_history'].append(("Bot", response.text))

# Display chat history in the sidebar
st.sidebar.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.sidebar.write(f"{role}: {text}")

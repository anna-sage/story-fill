import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


if "genre" not in st.session_state:
    st.session_state["genre"] = "anything"

with st.form("story_form"):
    genre_choice = st.selectbox("Select a genre", ["Fantasy", "Sci-fi", "Historical"])
    submit = st.form_submit_button("Go!")

if submit:
    st.session_state["genre"] = genre_choice
    st.header(st.session_state["genre"])
    response = model.generate_content(f"Write a concise yet cohesive 2 paragraph story in the {genre_choice} genre.")
    st.write(response.text)


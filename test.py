import streamlit as st
import os

# Get the GitHub token from the environment variable
github_token = os.getenv('GITHUB_TOKEN')

# Your app code
st.write("HELLO! WORRY NEVER HELPS")
st.write(f"Your GitHub token is: {github_token}")  # This line is just for testing; avoid exposing your token like this in production!

import streamlit as st

st.header("Readme")

def show_readme(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
        st.markdown(contents)

# Path to your readme.md file
readme_path = 'readme.md'

# Streamlit app
st.title('Readme Viewer')

# Display the contents of the readme.md file
show_readme(readme_path)
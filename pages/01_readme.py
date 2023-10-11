import streamlit as st

st.header("Readme")

def show_readme(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
        st.markdown(contents)


st.checkbox('portugues'.key='pt')

readme_path = 'README.md'
if st.session_state['pt']:
    readme_path = 'README_PT.md'

# Display the contents of the readme.md file
show_readme(readme_path)
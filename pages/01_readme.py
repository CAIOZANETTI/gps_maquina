import streamlit as st



def show_readme(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
        st.markdown(contents)

cols = st.columns([1,1])
cols[0].header("Readme")
cols[1].checkbox('portugues',key='pt')

readme_path = 'README.md'
if st.session_state['pt']:
    readme_path = 'README_PT.md'

# Display the contents of the readme.md file
show_readme(readme_path)
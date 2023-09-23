streamlit run [entrypoint Inicio.py]
import streamlit as st


def main():
    st.title("My Streamlit App")
    st.write("Welcome to my Streamlit app!")

if __name__ == "__main__":
    main()
"""

streamlit run [entrypoint Inicio.py]

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
) 

st.radio('idioma', ['ingles','português'],key='idioma')

"""
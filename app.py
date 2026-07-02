import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text into different languages")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Japanese": "ja"
}

text = st.text_area("Enter Text")

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):

    if text == "":
        st.warning("Please enter text")
    else:

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Successful")

        st.text_area(
            "Translated Text",
            translated,
            height=150
        )
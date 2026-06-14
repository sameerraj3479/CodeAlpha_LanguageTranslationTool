import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(page_title="AI Language Translation Tool")

st.title("🌍 AI Language Translation Tool")
st.write("Translate text and listen to the translated voice.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}

text = st.text_area("Enter Text")

st.write(f"Characters: {len(text)}")

source = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Target Language",
    list(languages.keys())
)

if st.button("Translate"):

    if text.strip():

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translated Text")

        st.write(translated)

        st.code(translated)

        try:
            tts = gTTS(
                text=translated,
                lang=languages[target]
            )

            tts.save("output.mp3")

            audio_file = open("output.mp3", "rb")

            st.audio(
                audio_file.read(),
                format="audio/mp3"
            )

        except Exception as e:
            st.error(f"Audio Error: {e}")

    else:
        st.warning("Please enter text.")
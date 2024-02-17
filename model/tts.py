from gtts import gTTS
import os
from model.generate_caption import *

LANGUAGES = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    # Potentially add more languages here
}

# Get the text to speech
def text_to_speech(text, lang='es', slow=False):
    tts = gTTS(text=text, lang=lang)
    return tts

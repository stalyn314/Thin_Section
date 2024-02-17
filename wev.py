import streamlit as st
import requests
import numpy as np
from PIL import Image
from model.generate_caption import *
from gtts import gTTS
import tempfile
import datetime
import psycopg2
import pandas as pd

st.title('Descripción automática de secciones delgadas de rocas')

    
uploaded_files = st.file_uploader("Carga imágenes de secciones delgadas de rocas", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("Nombre del archivo:", uploaded_file.name)
    print('Name of the file upload is: ',uploaded_file.name)
    location = f'Upload/{uploaded_file.name}'
    with open(os.path.join("Upload",uploaded_file.name),"wb") as f: 
      f.write(uploaded_file.getbuffer()) 
    pred_caption = generate_caption(location)

    tts = gTTS(pred_caption, lang='es', slow=False,tld='com.mx')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
      tts.save(fp.name)
      st.audio(fp.name, format="audio/mp3")
    
    print(type(bytes_data))
    st.image(location)
    st.write(pred_caption)
    st.write('____________________________________________________________________________________________')

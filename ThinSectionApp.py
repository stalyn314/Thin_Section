import streamlit as st
import requests
import numpy as np
from PIL import Image
from model.generate_caption import *
import datetime
import psycopg2
import pandas as pd

st.title('_Image_ Captioning Demo :sunglasses:')


# Connect to the database
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=2)
def run_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
    except psycopg2.ProgrammingError:
        st.success("Sucessfully Uploaded.")
        return None

uploaded_files = st.file_uploader("Upload some file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    print('Name of the file upload is: ',uploaded_file.name)
    location = f'Upload/{uploaded_file.name}'
    with open(os.path.join("Upload",uploaded_file.name),"wb") as f: 
      f.write(uploaded_file.getbuffer()) 
    pred_caption = generate_caption(location)
    query = f"INSERT INTO image_cap VALUES ('{uploaded_file.name}', '{location}', '{pred_caption}');"
    data = run_query(query)
    print(query)
    print(type(bytes_data))
    st.image(location)
    st.write(pred_caption)
    st.write('____________________________________________________________________________________________')

st.title('Uploaded')
rows = run_query("SELECT * from image_cap;")
df = pd.read_sql_query("SELECT * FROM image_cap", conn)

st.table(df)

st.title('Table of media')

for i in range(0,len(df['picture']),2): 
    cols = st.columns(2) 
    try: 
        cols[0].image(f'{df.picture[i]}', use_column_width=True)
        cols[0].text(f'{df.prediction[i]}')
        cols[1].image(f'{df.picture[i+1]}', use_column_width=True)
        cols[1].text(f'{df.prediction[i+1]}')
    except KeyError:
        pass


import os 
import requests

from PIL import Image
import streamlit as st 
from PIL import Image, ImageOps
 
import openai

openai.api_key=  st.secrets["apikey"]

st.title('😃😍🤩😉😎DALL-E: Generative AI -TEXT PROMPTS TO IMAGE')

prompts = st.text_input('Type the prompt')

if prompts: 

    response = openai.Image.create( prompt=prompts,  n=1,  size="1024x1024")
    image_url = response['data'][0]['url']
    st.image(image_url,use_column_width = True) 
    
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .css-1y0tads {padding-top: 0rem;}


            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


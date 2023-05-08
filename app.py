
import os 
import requests

from PIL import Image
import streamlit as st 
from PIL import Image, ImageOps
from apikey import apikey 
import openai
os.environ['OPENAI_API_KEY'] = apikey
model_engine = "text-davinci-003"
os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]

st.title('😃😍🤩😉😎DALLE: Revolutionary AI-Powered Learning Platform')

prompts = st.text_input('Type the prompt')

if prompts: 

    response = openai.Image.create( prompt=prompts,  n=1,  size="1024x1024")
    image_url = response['data'][0]['url']
    st.image(image_url,use_column_width = True) 


# import libraries
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
# load dotenv
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# create a model
model = genai.GenerativeModel('gemini-pro-vision')

# create  a response function
# if i only put image without promt then LLM model answer based on image information so i need to put prompt into that 

def response(x,y,z):
    ans = model.generate_content([x,y[0],z])
    return ans.text

def image_input_details(uploaded_file):
    if uploaded_file is not None:
        # read the file into bytes
        bytes_data= uploaded_file.getvalue()
        image_parts=[{
            'mime_type':uploaded_file.type,
            'data':bytes_data}
        ]
        return image_parts
    else:
        FileNotFoundError("no file uploaded")


# create a frontend
st.set_page_config(page_title='Invoice-Extractor')
st.header('Invoice-Extractor')
input= st.text_input("Ask a quetion")
# input image 
uploaded_file=st.file_uploader('choose a image')
image=''
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,use_container_width =True)
# st.image('image')
# create a prompt which give information to LLM how to answer 
prompt='''write a response based on input,this is the change
,'''
submit= st.button('submit')



if submit:
    image_data=image_input_details(image)
    text=response(prompt,image_data,input)
    st.write(text)
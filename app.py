import api
import streamlit as st #! creates front end for data sci projects
import os

#! to create interface
from streamlit chat import message
#! for styling
from streamlit extras.colored header import colored_header

os.environ['OPENAI_API_KEY']=api.get_key()

st.title("This is Sanya!!")

#! data,butto, sidebar etc
articles=st.selectbox("Choose a link",[
  'https://leetcode.com/u/sanya_851/',
  'https://gssoc.girlscript.tech/project',
  'https://www.youtube.com/watch?v=vIhDh7H73Ww&t=94s'
])

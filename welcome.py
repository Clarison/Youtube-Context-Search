import streamlit as st
from urllib.parse import urlparse, parse_qs

openai.api_key = st.secrets["openai_api_key"]
st.title("YouTube Transcript Embeddings Search")

video_url = st.text_input("Enter a YouTube video url:")

# get the video ID and channel from the URL
url_components = urlparse(video_url)
query_params = parse_qs(url_components.query)
video_id = query_params["v"][0]
channel = query_params["ab_channel"][0]

st.write(channel)
st.write(video_id)



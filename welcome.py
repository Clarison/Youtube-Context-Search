import streamlit as st
from urllib.parse import urlparse, parse_qs
st.title("YouTube Transcript Embeddings Search")

video_id = st.text_input("Enter a YouTube video url:")

# get the video ID and channel from the URL
url_components = urlparse(video_id)
query_params = parse_qs(url_components.query)
video_id = query_params["v"][0]
channel = query_params["ab_channel"][0]

st.write(channel)


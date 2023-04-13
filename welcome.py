import streamlit as st
from urllib.parse import urlparse, parse_qs
import openai

openai.api_key = st.secrets["openai_api_key"]
st.title("YouTube Transcript Embeddings Search")

video_url = st.text_input("Enter a YouTube video url:")



# get the video ID and channel from the URL
url_components = urlparse(video_url)
query_params = parse_qs(url_components.query)
video_id = query_params["v"][0]



st.write(video_id)

query = "what about Design Choice? "

res = openai.Completion.create(
    engine='text-davinci-003',
    prompt=query,
    temperature=0,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

st.write(res['choices'][0]['text'].strip())

def complete(prompt):
    # query text-davinci-003
    res = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return res['choices'][0]['text'].strip()

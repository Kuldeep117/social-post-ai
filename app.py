import streamlit as st
import urllib.request
import json
import os

st.title("AI Social Post Generator")
st.write("Topic likho - AI posts banayega!")

topic = st.text_input("Topic likho", placeholder="Cricket, Yoga, Business...")

if st.button("Generate Posts"):
    if topic:
        with st.spinner("Generating..."):
            try:
                api_key = os.environ.get("COHERE_API_KEY")
                url = "https://api.cohere.ai/v1/generate"
                payload = json.dumps({
                    "model": "command",
                    "prompt": "Create 5 viral social media posts about: " + topic + ". Add hashtags. Number 1-5.",
                    "max_tokens": 500
                }).encode()
                req = urllib.request.Request(url, data=payload, headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + api_key
                })
                with urllib.request.urlopen(req, timeout=30) as r:
                    result = json.loads(r.read())
                    st.write(result["generations"][0]["text"])
            except Exception as e:
                st.error(str(e))
    else:
        st.warning("Topic likho!")

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
                token = os.environ.get("HF_TOKEN")
                API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
                payload = json.dumps({"inputs": "Write 5 social media posts about " + topic}).encode()
                req = urllib.request.Request(API_URL, data=payload, headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + token
                })
                with urllib.request.urlopen(req, timeout=60) as r:
                    result = json.loads(r.read())
                    st.write(result[0]["generated_text"])
            except Exception as e:
                st.error(str(e))
    else:
        st.warning("Topic likho!")

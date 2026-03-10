import streamlit as st
import urllib.request
import json

st.title("AI Social Post Generator")
st.write("Topic likho - AI posts banayega!")

topic = st.text_input("Topic likho", placeholder="Cricket, Yoga, Business...")

if st.button("Generate Posts"):
    if topic:
        with st.spinner("Generating..."):
            API_URL = "https://api-inference.huggingface.co/models/facebook/opt-1.3b"
            payload = json.dumps({"inputs": "Create 5 viral social media posts about " + topic + " with hashtags numbered 1-5:"}).encode()
            try:
                req = urllib.request.Request(API_URL, data=payload, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=60) as r:
                    result = json.loads(r.read())
                    st.write(result[0]["generated_text"])
            except Exception as e:
                st.error(str(e))
    else:
        st.warning("Topic likho!")

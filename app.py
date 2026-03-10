import streamlit as st
import os
import urllib.request
import json

st.title("AI Social Post Generator")
st.write("Topic likho - AI posts banayega!")

topic = st.text_input("Topic likho", placeholder="Cricket, Yoga, Business...")

if st.button("Generate Posts"):
    if topic:
        with st.spinner("Generating..."):
            api_key = os.environ.get("GEMINI_API_KEY")
            url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + api_key
            data = '{"contents":[{"parts":[{"text":"Create 5 viral social media posts about: ' + topic + '. Add hashtags. Number 1-5."}]}]}'
            try:
                req = urllib.request.Request(url, data=data.encode(), headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=30) as r:
                    result = json.loads(r.read())
                    st.write(result["candidates"][0]["content"]["parts"][0]["text"])
            except Exception as e:
                st.error(str(e))
    else:
        st.warning("Topic likho!")

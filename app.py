import streamlit as st
import os
import urllib.request
import json

st.title("AI Social Post Generator")
st.write("Koi bhi topic likho - AI 5 viral posts banayega!")

topic = st.text_input("Topic likho", placeholder="Cricket, Yoga, Business...")

if st.button("Generate Posts"):
    if topic:
        api_key = os.environ.get("GEMINI_API_KEY")
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + api_key
        payload = json.dumps({"contents": [{"parts": [{"text": "Create 5 viral social media posts about: " + topic + ". Add hashtags. Number 1-5."}]}]}).encode()
        try:
            req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                result = json.loads(r.read())
                output = result["candidates"][0]["content"]["parts"][0]["text"]
                st.write(output)
        except Exception as e:
            st.error("Error: " + str(e))
    else:
        st.warning("Pehle topic likho

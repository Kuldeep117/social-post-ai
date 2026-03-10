import streamlit as st

st.title("AI Social Post Generator")
st.write("Topic likho - AI posts banayega!")

topic = st.text_input("Topic likho", placeholder="Cricket, Yoga, Business...")

if st.button("Generate Posts"):
    if topic:
        posts = f"""
1. {topic} ke baare mein yeh post hai! Bahut achha topic hai. #viral #{topic} #trending

2. Kya aap {topic} ke baare mein jaante hain? Yeh bahut interesting hai! #{topic} #india #viral

3. {topic} - ek aisa topic jo sabko pasand aata hai! #trending #{topic} #socialmedia

4. Aaj {topic} ke baare mein baat karte hain! Bahut important topic hai. #{topic} #viral #india

5. {topic} se related yeh jaankari aapke kaam aayegi! #{topic} #knowledge #trending
"""
        st.write(posts)
    else:
        st.warning("Topic likho!")

import streamlit as st
import pickle
import re

# Load saved model
model = pickle.load(open("spam_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub('[^a-z]', ' ', text)
    return text

st.title("📩 Spam Detection System")

msg = st.text_area("Enter your message:")

if st.button("Predict"):
    msg = clean_text(msg)
    vec = vectorizer.transform([msg])
    result = model.predict(vec)

    if result[0]==1:
        st.error("🚨 This is SPAM message")
    else:
        st.success("✅ This is HAM message")

import streamlit as st
import joblib

# ✅ Load model and vectorizer from the models directory
model = joblib.load("notebooks/sentiment_model.pkl")
vectorizer = joblib.load("notebooks/tfidf_vectorizer.pkl")


st.title("🧠 Stock Sentiment Predictor")
st.subheader("Enter a news headline or sentiment text:")

user_input = st.text_area("News or Sentiment Text", height=150)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]

        if prediction == 1:
            st.success("📈 The stock is likely to go UP!")
        else:
            st.error("📉 The stock is likely to go DOWN.")

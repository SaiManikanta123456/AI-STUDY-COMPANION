import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Load the MarianMT model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-fr"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Streamlit App
def main():
    st.title("Language Translation App")

    # Input text in English
    input_text = st.text_area("Enter English Text:", "Good morning")

    if st.button("Translate"):
        # Tokenize and translate
        inputs = tokenizer(input_text, return_tensors="pt")
        translation = model.generate(**inputs)
        translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)

        # Display translated text
        st.text_area("Translated Text:", translated_text)

if __name__ == "__main__":
    main()

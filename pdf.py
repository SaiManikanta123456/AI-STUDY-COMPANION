import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

st.title("PDF Text Search and Question Answering")

# Sidebar for uploading PDFs
st.sidebar.title("Upload PDFs")
pdf_files = st.sidebar.file_uploader("Choose up to 3 PDF files", accept_multiple_files=True, type="pdf")

# Function to process PDFs and display answer
def process_pdfs_and_answer(pdf_files, question):
    raw_text = ''

    # Read text from PDFs
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                raw_text += content

    # Split text into chunks and create embeddings
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)
    embeddings = OpenAIEmbeddings()
    document_search = FAISS.from_texts(texts, embeddings)

    # Load question answering chain and run the question
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    docs = document_search.similarity_search(question)
    result = chain.run(input_documents=docs, question=question)

    return result

# Main content
if pdf_files:
    # Allow the user to input a question
    question = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        # Process PDFs and display the answer
        result = process_pdfs_and_answer(pdf_files, question)
        st.write("### Answer:")
        st.write(result)
else:
    st.write("Please upload PDFs in the sidebar.")

# import streamlit as st
# from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig
# import torch
# import pickle
#
# # Load the tokenizer from file
# with open("bart_tokenizer.pkl", "rb") as f:
#     tokenizer = pickle.load(f)
#
# # Load the model
# config = BartConfig()  # Create a default configuration
# model = BartForConditionalGeneration(config)  # Initialize the model with the configuration
# model.load_state_dict(torch.load("bart_model_state_dict.pth"))
# model.eval()
#
# # Function to generate summary
# def generate_summary(input_text):
#     inputs = tokenizer([input_text], max_length=1024, return_tensors="pt", truncation=True)
#     summary_ids = model.generate(inputs["input_ids"], max_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary
#
# # Main content
# st.title("Text Summarizer")
# user_text = st.text_area("Enter your text:")
#
# if user_text:
#     if st.button("Generate Summary"):
#         summary_result = generate_summary(user_text)
#         st.write("### Summary:")
#         st.write(summary_result)


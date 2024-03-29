#
# import openai
# import streamlit as st
# from dotenv import load_dotenv
# import os
#
# # Set your OpenAI API key here
#
# load_dotenv()
#
# openai.api_key = os.getenv("OPENAI_API_KEY")
#
# # Initialize Streamlit app title
# st.title("Student Assistant")
#
# # Initialize variables if not present in session state
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"
#
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#
# # Get user input
# if prompt := st.chat_input("Ask a question related to data science or machine learning"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)
#
#     # Generate assistant response
#     with st.spinner("Hold on a moment saii...."):
#         assistant_response = openai.ChatCompletion.create(
#             model=st.session_state["openai_model"],
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ]
#         )['choices'][0]['message']['content']
#
#     # Display assistant response
#     with st.chat_message("assistant"):
#         st.markdown(assistant_response)
#
#     st.session_state.messages.append({"role": "assistant", "content": assistant_response})
import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Set your OpenAI API key here
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Streamlit app title
st.title("Student Assistant")

# Initialize variables if not present in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Create a sidebar to select multiple subjects
selected_subjects = st.sidebar.multiselect(
    "Select Subjects:",
    ["Data Science", "Computer Networks","Operating Systems","Java","C++","Automata Theory", "Python", "Statistics", "NLP"],
)

# Check if at least one subject is selected
if selected_subjects:
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get user input
    if prompt := st.chat_input("Ask a question related to selected subjects"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate assistant response
        with st.spinner("Hold on a moment saii..."):
            # Check if the subjects are among the prescribed subjects
            valid_subjects = ["Data Science", "Computer Networks","Operating Systems","Java","C++","Automata Theory", "Python", "Statistics", "NLP"]
            for subject in selected_subjects:
                if subject not in valid_subjects:
                    st.error("Subject not prescribed. Please select valid subjects from the sidebar.")
                    st.session_state.messages.append({"role": "assistant", "content": "Subject not prescribed."})
                    break
            else:
                assistant_response = openai.ChatCompletion.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ]
                )['choices'][0]['message']['content']

                # Display assistant response
                with st.chat_message("assistant"):
                    st.markdown(assistant_response)

                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    # Add a button to download the whole chat as a text file
    if st.button("Download Chat"):
        chat_history = "\n".join([f"{message['role']}: {message['content']}" for message in st.session_state.messages])
        st.download_button(
            label="Download Chat",
            data=chat_history,
            key="download_chat.txt",
            on_click=None,
            help="Download the entire chat as a text file.",
        )

else:
    st.sidebar.info("Select one or more subjects from the sidebar to get started.")

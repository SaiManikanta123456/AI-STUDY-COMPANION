
import streamlit as st
import subprocess
#
# def main():
#     st.title("Student Companion🫂")
#
#     options = ["Chat Bot 🤖", "URL Explorer🕸️", "PDF's FRIEND📃","Mail Maker✉"]
#
#     # Display options horizontally using Streamlit columns
#     col1, col2, col3 ,col4= st.columns(4)
#     with col1:
#         if st.button(options[0]):
#             subprocess.run(["streamlit", "run", "chat.py"])
#
#     with col2:
#         if st.button(options[1]):
#             subprocess.run(["streamlit", "run", "Langchain.py"])
#
#     with col3:
#         if st.button(options[2]):
#             subprocess.run(["streamlit", "run", "pdf.py"])
#     with col4:
#         if st.button(options[3]):
#             subprocess.run(["streamlit", "run", "mail_maker.py"])
# if __name__ == "__main__":
#     main()



import streamlit as st
import subprocess
import base64
import streamlit as st
import subprocess

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
# add_bg_from_local(r"D:\python\Face1\TECH-CHAT\Untitled design.png")


st.markdown("""
<style>
.chat{
font-size:20px !important;
font-family:sans-serif;
color:orange;
font-weight:bold;
}
.main1{
font-size:40px !important;
font-family:sans-serif;
color:red;
text-align:center;
font-weight:bold;
}
.c1{
font-size:20px !important;
font-family:sans-serif;
font-weight:bold;
}
.c2{
font-size:16px !important;
font-family:sans-serif;
color:yellow;
}
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<p class="main1">STUDENT SIMPLIFY</p>',unsafe_allow_html=True)

    options = ["Chat Bot 🤖", "URL Explorer🕸️", "PDF's FRIEND📃", "Mail Maker✉"]

    # Add custom CSS to create vertical lines across the entire page
    st.markdown(
        """
        <style>
        .css-1v5m7av {
            border-right: 1px solid #ccc;
            padding-right: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display options and descriptions
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<p class="chat">CHATIFY</p>',unsafe_allow_html=True)
        if st.button(options[0]):
            pass
            # subprocess.run(["streamlit", "run", "chat.py"])
        st.markdown('<p class="c1">Chat with our friendly chat bot.</p>',unsafe_allow_html=True)

        st.write('<p class="c2">Select the subjects from dropdown</p>',unsafe_allow_html=True)
        st.write('<p class="c2">Ask questions and Get the answers🥳🎉</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Copy 📄the entire chat for further use.</p>', unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="chat">WEBIFY</p>', unsafe_allow_html=True)
        if st.button(options[1]):
            pass
            # subprocess.run(["streamlit", "run", "Langchain.py"])
        st.markdown('<p class="c1">Explore URLs</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Paste the URLs that are tedious to read</p>', unsafe_allow_html=True)
        st.write('<p class="c2">click 👆 on Process URLs</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Ask questions and Get the answers🥳🎉</p>', unsafe_allow_html=True)

    with col3:
        st.markdown('<p class="chat">DOCIFY</p>', unsafe_allow_html=True)
        if st.button(options[2]):
            pass
            # subprocess.run(["streamlit", "run", "pdf.py"])
        st.markdown('<p class="c1">PDF utility</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Give us the heavy PDFs🤯</p>', unsafe_allow_html=True)
        st.write('<p class="c2"> Give a simple click 👆 to Process them</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Ask questions and Get the answers🥳🎉</p>', unsafe_allow_html=True)

    with col4:
        st.markdown('<p class="chat">MAILIFY</p>', unsafe_allow_html=True)
        if st.button(options[3]):
            pass
            # subprocess.run(["streamlit", "run", "mail_maker.py"])
        st.markdown('<p class="c1">Create EMAILs</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Write a simple reason for mail</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Tell us word limit and to whom you are writing mail</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Relax 😎 for a couple of seconds to make up mail</p>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()

# import streamlit as st
# import subprocess
#
# CSS = """
# <style>
# .button-container {
#     position: relative;
#     display: inline-block;
#     margin: 10px;
# }
#
# .button-description {
#     display: none;
#     position: absolute;
#     background-color: #f9f9f9;
#     padding: 10px;
#     border: 1px solid #ccc;
#     border-radius: 5px;
#     z-index: 1;
# }
#
# .button-container:hover .button-description {
#     display: block;
# }
# </style>
# """
#
# def main():
#     st.title("Student Companion🫂")
#     st.write(CSS, unsafe_allow_html=True)
#
#     options = {
#         "Chat Bot 🤖": "Description for Chat Bot",
#         "URL Explorer🕸️": "Description for URL Explorer",
#         "PDF's FRIEND📃": "Description for PDF's FRIEND"
#     }
#
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         button1 = st.button(list(options.keys())[0], key='button1', on_click=None)
#         if button1:
#             subprocess.run(["streamlit", "run", "chat.py"])
#         st.markdown(f'<div class="button-description">{options[list(options.keys())[0]]}</div>', unsafe_allow_html=True)
#
#     with col2:
#         button2 = st.button(list(options.keys())[1], key='button2', on_click=None)
#         if button2:
#             subprocess.run(["streamlit", "run", "Langchain.py"])
#         st.markdown(f'<div class="button-description">{options[list(options.keys())[1]]}</div>', unsafe_allow_html=True)
#
#     with col3:
#         button3 = st.button(list(options.keys())[2], key='button3', on_click=None)
#         if button3:
#             subprocess.run(["streamlit", "run", "pdf.py"])
#         st.markdown(f'<div class="button-description">{options[list(options.keys())[2]]}</div>', unsafe_allow_html=True)
#
# if __name__ == "__main__":
#     main()
#
#
#
import streamlit as st
import subprocess
# HTML and CSS for the zoom-out effect
# zoom_out_css = """
# <style>
# .button {
#   background-color: #008CBA;
#   border: none;
#   color: white;
#   text-align: center;
#   text-decoration: none;
#   display: inline-block;
#   font-size: 16px;
#   margin: 4px 2px;
#   cursor: pointer;
#   border-radius: 12px;
#   padding: 10px 24px;
#   transition: transform 0.3s ease-in-out;
# }
#
# .button:hover {
#   transform: scale(1.3);
#   background-color: skyblue;
# }
# </style>
# """

# Display the button with the zoom-out effect
# st.markdown(zoom_out_css, unsafe_allow_html=True)
# col1, col2, col3 = st.columns(3)
# button_hover_1 = '<button class="button">Chat Bot 🤖</button>'
# st.markdown(button_hover_1, unsafe_allow_html=True)
# button_hover_2 = '<button class="button">URL Explorer🕸️</button>'
# st.markdown(button_hover_2, unsafe_allow_html=True)
# button_hover_3 = '<button class="button">PDFs FRIEND📃</button>'
# st.markdown(button_hover_3, unsafe_allow_html=True)
# with col1:
#     if button_hover_1:
#         subprocess.run(["streamlit", "run", "chat.py"])
# with col2:
#     if button_hover_2:
#         subprocess.run(["streamlit", "run", "Langchain.py"])
# with col3:
#     if button_hover_3:
#         subprocess.run(["streamlit", "run", "pdf.py"])

# import streamlit as st
# import subprocess
# # HTML and CSS for the zoom-out effect
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
#   transform: scale(1.5);
# }
# </style>
# """
#
# # Display the button with the zoom-out effect
# st.markdown(zoom_out_css, unsafe_allow_html=True)
# button_hover_1 = '<button class="button">Chat Bot 🤖</button>'
# st.markdown(button_hover_1, unsafe_allow_html=True)
# button_hover_2 = '<button class="button">URL Explorer🕸️</button>'
# st.markdown(button_hover_2, unsafe_allow_html=True)
# button_hover_3 = '<button class="button">PDFs FRIEND📃</button>'
# st.markdown(button_hover_3, unsafe_allow_html=True)
#
# if button_hover_1:
#     subprocess.run(["streamlit", "run", "pdf.py"])
import streamlit as st
from streamlit_option_menu import option_menu
selected=option_menu(
    menu_title=None,
    options=['Home','Services','Contact'],
    icons=['house','car-front','phone'],
    orientation="horizontal"
)
if selected=='Home':
    st.markdown('Its Home man')
if selected=='Services':
    st.markdown('Its Services man')
if selected=='Contact':
    st.markdown('Its contacts man')

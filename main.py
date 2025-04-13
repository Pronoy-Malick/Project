import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500, output_format="auto")

with col2:
    st.title("Pronoy Malick")
    content1 = """I am a Python Developer(Intermediate). I complete my Graduation in B.Tech in Computer Science Engineering in St.Thomas' College of Engineering and Technology 
     under the MAKAUT University which is situated in Kolkata, West Bengal.Here I attached all my project I did so far. Hope this 
    helps you to judge me in a better way. I tried my level best in doing all these projects. I tried my level
    best to cover all type of projects through PYTHON"""

    st.info(content1)

content2 = """ Here below are attached my App and Websites I build so far. Feel free to Contact me"""
st.write(content2)
import streamlit as st
import pandas


st.set_page_config(layout="centered")

content2 = """ Explore My Projects below"""
st.header(content2)

col3,empty_col, col4 = st.columns([4,1,4])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])
        # st.info(row["description"])
        st.image("images/" + row["image"], width=100)
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Source Code",row["url"], help="Go to Github")
        with col2:
            st.link_button("Live Demo",row["demo"], help="Shows the demo")

with col4:
    for index, row in df[10:].iterrows():
        st.subheader(row["title"])
        # st.info(row["description"])
        st.image("images/" + row["image"], width=100)
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Source Code", row["url"], help="Go to Github")
        with col2:
            st.link_button("Live Demo", row["demo"], help="Shows the demo")

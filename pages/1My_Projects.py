import streamlit as st
import pandas



content2 = """ Explore My Projects below"""
st.header(content2)

col3,empty_col, col4 = st.columns([2,2,2])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])
        st.info(row["description"])
        st.image("images/" + row["image"])
        st.link_button("Source Code",row["url"], help="Go to Github")

with col4:
    for index, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.info(row["description"])
        st.image("images/" + row["image"])
        st.link_button("Source Code",row["url"], help="Go to Github")
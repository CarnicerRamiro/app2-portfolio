import streamlit as st
import pandas


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Juancito")
    content1 = """
    Soy alto dev vieja, no te das una idea de como la marco!!!
    """
    st.info(content1)

content2 = """
Ahora tengo que explicarte toda la mierda que hize, re loca. Dale que vamos!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

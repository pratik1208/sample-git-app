import streamlit as st
st.title('CampusX')

col1, col2 = st.columns(2)

with col1:
    st.image('images.png')
with col2:
    st.header('I love quotes')
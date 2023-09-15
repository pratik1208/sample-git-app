import streamlit as st
st.title('CampusX')

col1, col2 = st.columns(2)

with col1:
    st.image('unnamed.png')
with col2:
    st.header('I love quotes')

st.header('Courses')
st.sidebar.title('menu')
st.subheader("DSA")
st.subheader("DBMS")
st.subheader("DSMP")

st.sidebar.markdown("""
- Home
- About
- Contact
- career
- Login
"""
)


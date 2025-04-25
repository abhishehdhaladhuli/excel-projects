import streamlit as st
st.title("My first python app using streamlit ")
st.write("Hello world")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is a markdown")
st.caption("This is a caption")
st.code("print('Hello world')")
value=st.text_input("Enter your name")
st.divider()
button=st.button("Click me")
if button:
    st.write(f"Hello {value}")
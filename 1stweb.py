import streamlit as st


# st.title("Welcome to nusrat 1st website")
# st.header("Python")
# st.subheader("java")
#
# st.markdown("I love python")
# st.code("""for i im range(1,5,1):
#                 print("hello")
#                 """)

name = st.text_input("Enter Your name:")
fname = st.text_input("Enter your father name:")
adr = st.text_area("Enter your address:")
classdata = st.selectbox("enter your class:",(1,2,3,4,5,6))


btn = st.button("Done")
if btn:
    st.markdown(f"""
    Name : {name}
    Father Name : {fname}
    Adrress : {adr}
    class : {classdata}""")
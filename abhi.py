import streamlit as st
st.title("Abhilekha Priyadarshini")

def generate_pattern(user_input):
    for i in range(1, len(user_input)+1):
        return user_input[:i]

st.title("Generate Pattern")
user_input = input()

for i in generate_pattern(user_input):
    st.write(i)

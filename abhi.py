import streamlit as st
st.title("Abhilekha Priyadarshini")

def generate_pattern(user_input):
    for i in range(len(user_input)+1):
        return user_input[:i]

st.title("Generate Pattern")

user_input = st.text_input("Your Text:")

if user_input:
    result = generate_pattern(user_input)
    st.text("Generated Pattern:")
    for line in result:
        st.write(line)




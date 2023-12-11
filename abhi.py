import streamlit as st
from pattern_generator import generate_pattern

st.title("Pattern Generator with Streamlit")

# Streamlit input
user_input = st.text_input("Enter a string:")
result = generate_pattern(user_input)

# Display the output in Streamlit
st.text("Generated Pattern:")
for line in result:
    st.text(line)


def generate_pattern(input_str):
    for i in range(1,len(n)+1):
        return n[:i]

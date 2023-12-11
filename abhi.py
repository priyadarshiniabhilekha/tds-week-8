def generate_pattern(input_str):
    length = len(input_str)
    pattern_list = []

    for i in range(1, length + 1):
        pattern_list.append(input_str[:i])

    return pattern_list

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = generate_pattern(user_input)
    
    for line in result:
        print(line)

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


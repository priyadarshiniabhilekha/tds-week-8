# app.py

import streamlit as st
st.title("TDS week 8 assignment by Abhilekha Priyadarshini'22F1000350'")

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find Largest"):
        result = find_largest(num1, num2, num3)
        st.success(f"The largest number is: {result}")

if __name__ == "__main__":
    main()





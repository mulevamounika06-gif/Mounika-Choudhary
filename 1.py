import streamlit as st
st.title("welcome to streamlit")
num1=st.number_input("enter the number 1")


num2=st.number_input("enter the number 2")
sum=num1+num2
if st.button("add"):
    print(sum)
    st.write("sum is sum",sum)
    

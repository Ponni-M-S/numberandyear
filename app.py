
    
    
    
    
    
    
import streamlit as st

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


    
year = st.number_input("Enter a year:", min_value=1, step=1)

if st.button("Check"):
    if is_leap_year(year):
            st.write(f"{year} is a leap year!")
    else:
            st.write(f"{year} is not a leap year.")

number = st.number_input("Enter a number:",value=0)
    
if number % 2 == 0:
        st.write(f"{number} is an even number.")
else:
        st.write(f"{number} is an odd number.")


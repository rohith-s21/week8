import streamlit as st

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    st.title('Find the Largest Among Three Numbers')

    num1 = st.number_input('Enter the first number')
    num2 = st.number_input('Enter the second number')
    num3 = st.number_input('Enter the third number')

    if st.button('Find Largest'):
        largest = find_largest(num1, num2, num3)
        st.write(f'The largest number among {num1}, {num2}, and {num3} is: {largest}')

if __name__ == '__main__':
    main()
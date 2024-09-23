import streamlit as st
import pandas as pd
import numpy as np

# Set title for the Streamlit app
st.title("Basic Streamlit App")

# Displaying some text
st.write("This is a basic Streamlit app!")

# Taking user input
name = st.text_input("Enter your name:", "Type here...")

# Display the input
if name:
    st.write(f"Hello, {name}!")

# Creating a random dataframe
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)

# Displaying a table
st.write("Here is a random table of data:")
st.write(data)

# Plotting a simple chart
st.line_chart(data)

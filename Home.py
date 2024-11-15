import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text
comp_name = "The Best Company"
comp_descr = """
The Best Company elevators, escalators, and moving walks transport more than 2 billion 
of us up and down buildings and across transportation hubs every day. Together 
with our customers, we help organize cities: by moving people and goods, and by 
connecting vertical and horizontal transportation systems.
"""
st.header(comp_name)
st.write(comp_descr)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv", sep=',')

with col1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"].title() + ' ' + row['last name'].title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'])

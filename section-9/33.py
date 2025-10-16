# section-9/33.py
# Streamlit Basics
# run:>  streamlit run 33.py

import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello Streamlit')
st.write('Hey this is a simple text')

df = pd.DataFrame({'first column': [1, 2, 3], 'second column': [4, 5, 6]})
st.write('Here is the data frame:')
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
st.bar_chart(chart_data)


name = st.text_input('Enter your name')
if name:
    st.write(f'Hello {name}')


age = st.slider('Select your age', 0, 100, 25)
st.write(f'Your age is {age}')

options = ['Python', 'Java', 'C', 'C++', 'JavaScript']
choice = st.selectbox('Choose your favorite programming language', options)
st.write(choice)

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)


color = st.color_picker("Pick a color")
st.write(f'You selected: {color}')

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
elif genre == "***Drama***":
    st.write("You selected drama.")
elif genre == "Documentary :movie_camera:":
    st.write("You selected documentary.")
else:
    st.write("You didn't select a genre.")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )


import datetime

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)    

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d



d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)
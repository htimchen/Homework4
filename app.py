# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

#Question 1
st.title("Homework 4")

#Question 2
st.markdown("[Helen Timchenko] (https://github.com/htimchen)")

#Question 3
uploaded_file = st.file_uploader("Input CSV", type= "csv")

#Question 4
#Convert file into pandas dataframe
#But there will be an error if we don't have an uploaded file first
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

#Question 5
#If x is an empty string, make it numpy's not-a-number
#otherwise, leave x alone
    df = df.applymap(lambda x: np.nan if x == " " else x )

#Question 6
    #c is a col name
    #See Week 3 Friday notes
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
    #now let's make a list of all cols that can be numeric
    good_cols = [c for c in df.columns if can_be_numeric(c)]

#Question 7
#Replace cols in df that can be made numeric with numeric values
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis = 0)
    #df_good = df[good_cols]

#Question 8
#Select x-axis and y-axis from st.selectbox
    x_axis = st.selectbox("Choose an x-value",good_cols)
    y_axis = st.selectbox("Choose a y-value",good_cols)
    
#Question 9
    slider = st.slider("Select range of rows:", 0 , len(df.index)-1, (0, len(df.index)-1))
    #r = df.iloc[slider]

#Question 10 -The song in the nth postion is {song name} by {artist}.
    #st.write(f"The user chose {slider}")
    artist = list(df["Artist"])
    song = list(df["Song Name"])
    def a(n):
        return artist[n]
    def s(n):
        return song[n]
    st.write(f"The song in the {slider}th position is {s(slider[0])} by {a(slider[0])}.")

#Question 11
    my_chart = alt.Chart(df.loc[slider[0]:slider[1]]).mark_circle().encode(
        x = x_axis,
        y = y_axis,
        tooltip = ["Artist", "Song Name"]
    )
    st.altair_chart(my_chart)

#Question 12 is the tooltip in the chart

#Bonus - This is for me to see the version for the requirement
st.write(st.__version__)
st.write(np.__version__)
st.write(pd.__version__)
st.write(alt.__version__)
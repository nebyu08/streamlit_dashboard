import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#lets write
st.write("this is a **text** and u to italian **_italic_**")

#this is the dataframe
df=pd.read_csv(r"C:/Users/dread-miles/Documents/Data Sets/diabetes.csv")

st.write(df)

fig,ax=plt.subplots()

ax.scatter(np.arange(5),np.arange(5)**2)

st.write(fig)

st.title("this is a title")

st.header("this is the header")

st.subheader("this is the subheader")

code=''' def square(x):
    return x**2'''

st.code(code,language='python')
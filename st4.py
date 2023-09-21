import streamlit as st
import pandas as pd
import numpy as np
import time

#st.write(time.time())
#bt=st.button("Click Me")
#st.write(bt)

def fn():
    st.write(time.time())
    
st.button("Click Me",on_click=fn)

#dawnloadinf dataframe in a csv format
df=pd.DataFrame(np.random.randn(10,2),columns=['col1','col2'])

data=df.to_csv().encode('utf-8')

st.download_button(
    label='dawnload file',
    data=data,
    file_name="new_file.csv",
    mime="text/csv"
    )
#downloding an image
file=open("C:/Users/dread-miles/Pictures/Wallpaper/737400.jpg","rb")
st.download_button(
    label="download image",
    data=file,
    file_name="anime.jpg",
    mime="image/jpg"
)

#lets try the check boc
ck=st.checkbox("i agree")

if ck == True:
    st.write("you have completed the form")
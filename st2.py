
import streamlit as st
import numpy as np
import pandas as pd
import json

#st.write("hello there")

df=pd.DataFrame(
    np.random.rand(50,20),
    columns=["col " +str(i) for i in range(20) ]
    )

# this is managing dataframe in streamlit
st.dataframe(df,width=200,height=210)
st.dataframe(np.random.randn(50,20))

#this is managing table in streamlit
st.table(df)

#metric managment in streamlit
st.metric("TESLA.LLC",value="3000",delta="23.45",delta_color="inverse")
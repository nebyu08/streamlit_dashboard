
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

df=pd.DataFrame(np.random.randn(10,2),columns=["price","diff"])

#lets plot line chart
st.line_chart(df,y=['price'])

#lets plot the area chart
st.area_chart(df,y=['diff'])

#lets plot the bar chart
st.bar_chart(df,y=['diff'])

#lets plot a pyplot 
fig,ax=plt.subplots()
ax.scatter(np.arange(10),np.arange(10)**2)
st.pyplot(fig)

#lets do one for histograph
fig,ax=plt.subplots()
ax.hist(np.random.randn(100),bins=10)
st.pyplot(fig)

#lets check out our map
st.map()
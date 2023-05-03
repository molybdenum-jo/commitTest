import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('고객분석')
st.sidebar.title('고객분석')

st.write("""
### DATA 전처리
- 0세 => 15세(상위1%)
- 80세 이상(하위4%이상) => 80세
""")

st.write("""
### Dataset
""")
df_train = pd.read_csv('data/AGE.csv')
st.dataframe(df_train)

st.write(""" 
### part 1. 나이별 분석
""")
df = pd.read_csv('data/AGE.csv')

fig2 = px.bar( df, x='Age', y='Count')        #plotly bar차트
st.plotly_chart(fig2)



st.write(""" 
### part 2. 지역별 분석
""")


st.write(""" 
### part 3. 유저 분석 
""")

import streamlit as st
import pandas as pd
import numpy as np


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

df['Age'].plot.hist(bins=30) # 히스토그램 그리기
plt.title('Age Distribution') # 그래프 제목 설정
plt.xlabel('Age') # x축 레이블 설정
plt.ylabel('Count') # y축 레이블 설정
plt.show() # 그래프 보이기


st.write(""" 
### part 2. 지역별 분석
""")


st.write(""" 
### part 3. 유저 분석 
""")

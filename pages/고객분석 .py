import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('고객분석')
st.sidebar.title('고객분석')
st.sidebar.subheader("part 1. 나이별 분석")
st.sidebar.markdown("""
    ## Table of Contents
    - [Part 1. Age Analysis](#part-1-age-analysis)
    - [Part 2. Gender Analysis](#part-2-gender-analysis)
""")
st.sidebar.subheader("part 2. 지역별 분석")
st.sidebar.subheader("part 3. 유저 분석 ")

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

# part 1
st.write(""" 
### part 1. 나이별 분석
""")
st.write('<div id="part-1"></div>', unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('data/AGE.csv')

# 히스토그램 그리기
fig4 = plt.figure()
plt.hist(data=df, x='Age', bins=30, rwidth=0.8)
plt.title('Age Distribution') # 그래프 제목 설정
plt.xlabel('Age') # x축 레이블 설정
plt.ylabel('Count') # y축 레이블 설정

# 그래프 표시하기
st.pyplot(fig4)




st.write(""" 
### part 2. 지역별 분석
""")


st.write(""" 
### part 3. 유저 분석 
""")

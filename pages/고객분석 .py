import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('고객분석')
st.sidebar.title('고객분석')
st.sidebar.markdown("""
    ## Table of Contents
    - [part 1. 나이별 분석](#part-1-age-analysis)
    - [part 2. 지역별 분석](#part-2-location-analysis)
    - [part 3. 유저별 분석](#part-3-user-analysis)
""")

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

### Part 1. 나이별 분석
st.markdown("<h1 id='part-1-age-analysis'>Part 1. 나이별 분석</h1>", unsafe_allow_html=True)

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

### Part 2. 지역별 분석
st.markdown("<h1 id='part-2-location-analysis'>Part 2. 지역별 분석s</h1>", unsafe_allow_html=True)

### Part 3. 유저별 분석
st.markdown("<h1 id='part-3-user-analysis'>Part 3. 유저별 분석</h1>", unsafe_allow_html=True)

# 소제목 클릭 시 해당 위치로 이동
if st.sidebar.button("Part 1. 나이별 분석"):
    js = "window.scrollTo(0, document.getElementById('part-1-age-analysis').offsetTop);"
    html = '<script>{}</script>'.format(js)
    st.markdown(html, unsafe_allow_html=True)

if st.sidebar.button("Part 2. 지역별 분석"):
    js = "window.scrollTo(0, document.getElementById('part-2-location-analysis').offsetTop);"
    html = '<script>{}</script>'.format(js)
    st.markdown(html, unsafe_allow_html=True)
    
if st.sidebar.button("Part 3. 유저별 분석"):
    js = "window.scrollTo(0, document.getElementById('part-3-user-analysis').offsetTop);"
    html = '<script>{}</script>'.format(js)
    st.markdown(html, unsafe_allow_html=True)
    

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('고객분석')
st.sidebar.title('고객분석')
st.sidebar.markdown('[This is a link](#category1)')
category = st.sidebar.radio(
    'Select a category:',
    ['Category 1', 'Category 2', 'Category 3']
)

# 선택한 카테고리에 따라 출력
if category == 'Category 1':
    st.write('You selected Category 1')
elif category == 'Category 2':
    st.write('You selected Category 2')
elif category == 'Category 3':
    st.write('You selected Category 3')

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

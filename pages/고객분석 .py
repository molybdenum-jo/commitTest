import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('고객분석')
st.sidebar.title('고객분석')
st.sidebar.markdown("""
    ## 고객 분석
    - [part 1. 나이별 분석](#part-1-age-analysis)
    - [part 2. 지역별 분석](#part-2-location-analysis)
    - [part 3. 유저별 분석](#part-3-user-analysis)
""")

st.write("""
### DATA 전처리

- 의견1) 0세는 상위1% 값이 15세로 대체. 모두 하위 4%와 3% 구간 사이에서 비교적 급격한 나이 변화가 일어났으므로 급격한 나이변화가 일어나는 구간부터는 모두 이상치로 판단, 따라서 하위4% 이하인 80세 이상은 모두 80세로 대체
- 의견2) 상위 1%인 0-15세를 모두 15세로 대체하며, 하위1%에 해당하는 67세-244세는 모두 67세로 대체
- 의견3) 나이별 사분위수 와 threshold사용

-> 모델 예측점수 결과가 가장 좋았던 의견 1)을 사용하기로 함

""")

st.write("""
### Dataset
""")
df_train = pd.read_csv('data/AGE.csv')
st.dataframe(df_train)


js = "window.scrollTo(0, document.getElementById('part-1-age-analysis').offsetTop);"

    
st.markdown("<h3 id='part-1-age-analysis'>Part 1. 나이별 분석</h3>", unsafe_allow_html=True)



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('data/AGE.csv')

# 히스토그램 그리기
fig4, ax = plt.subplots(figsize=(10, 6))
ax.hist(data=df, x='Age', bins=30, rwidth=0.8)
ax.set_title('Age Distribution') # 그래프 제목 설정
ax.set_xlabel('Age') # x축 레이블 설정
ax.set_ylabel('Count') # y축 레이블 설정

# 그래프 표시하기
st.pyplot(fig4)


### Part 2. 지역별 분석
st.markdown("<h1 id='part-2-location-analysis'>Part 2. 지역별 분석s</h1>", unsafe_allow_html=True)

### Part 3. 유저별 분석
st.markdown("<h1 id='part-3-user-analysis'>Part 3. 유저별 분석</h1>", unsafe_allow_html=True)


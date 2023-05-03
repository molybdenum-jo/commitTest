import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('고객분석')
st.sidebar.title('고객분석')

if st.sidebar.button('part 1. 나이별 분석'):
    js = "window.scrollTo(0, document.getElementById('part-1-나이별-분석').offsetTop);"
    # 버튼 클릭 시 이동 함수 호출
    html = '<script>{}</script>'.format(js)
    st.markdown(html, unsafe_allow_html=True)
    st.write('You clicked Category 1!')

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
<div id='part-1-나이별-분석'></div> # 제목 위 위치에 해당하는 div 태그
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

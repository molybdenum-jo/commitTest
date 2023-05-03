import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('📖출판사분석')


st.sidebar.markdown("""
    ## 고객 분석
    - [part 1. 도서 분석](#part-1-book-analysis)
    - [part 2. 작가 분석](#part-2-author-analysis)
    - [part 3. 출판년도 분석](#part-3-year_publication-analysis)
    - [part 4. 출판사 분석](#part-3-publisher-analysis)
""")
st.write('')
st.write("""
- 출판사나 도서 기업의 입장에서 도서 평점을 활용한 분석이다. 출판사/도서기업이 가지고 있는 고객 데이터와 평점 등을 통해 출판사/도서기업의 데이터가 고객의 평점에 어떠한 영향을 미치는지를 분석하여 고객의 선호도를 분석한다.

""")
st.write('')
st.write('')


js = "window.scrollTo(0, document.getElementById('part-1-age-analysis').offsetTop);"

    
st.markdown("<h3 id='part-1-age-analysis'>✅Part 1. 도서 분석</h3>", unsafe_allow_html=True)

st.write('')
st.write('')
st.write("""

- 예를들어 Harry Potter 단어가 포함된 단어를 찾으면 해당 정보를 아래와 같이 찾을 수 있음
- 같은 책이라도 에디션에 따라 나뉘는 종류가 다르게 경우가 있다
""")

st.write("""
##### ✔ 상위 10위 도서별 평점수

""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_book = pd.read_csv('data/popbooks.csv')

fig1, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='N_rating', y='Book-Title', data=df_book,palette='Set1')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Top10 Books most read by users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig1)

st.write("""
##### ✔ 상위 10위 도서별 평균 평점

""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_avg = pd.read_csv('data/goodratingbooks.csv')

fig3, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='avg_rating', y='Book-Title', data=df_avg,palette='Set1')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Top10 Books most read by users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig3)

st.write('')
st.write('')
js = "window.scrollTo(0, document.getElementById('part-2-location-analysis').offsetTop);"
  
st.markdown("<h3 id='part-2-author-analysis'>✅Part 2. 작가 분석</h3>", unsafe_allow_html=True)

st.write("""

- 같은 저자라도 J.K Rowling, Joanne K,Rowling, Joanne K.Rowling과 같이 다른 방식으로 표기가 되어있는 경우가 있다
""")

st.write("""
##### ✔ 상위10위 작가별 평균 평점

""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_author = pd.read_csv('data/goodratingbooks.csv')

fig2, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='avg_rating', y='Book-Author', data=df_author,palette='Set1')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Top 10 Book of rating by author', fontsize=16)

# 그래프 표시하기
st.pyplot(fig2)


js = "window.scrollTo(0, document.getElementById('part-3-user-analysis').offsetTop);"

st.markdown("<h3 id='part-3-user-analysi'>✅Part 3. 유저별 분석</h3>", unsafe_allow_html=True)
st.write("""
#### DATA 전처리

- 예를들어 Harry Potter 단어가 포함된 단어를 찾으면 해당 정보를 아래와 같이 찾을 수 있음
- 같은 책이라도 에디션에 따라 나뉘는 종류가 다르게 경우가 있다
- 같은 저자라도 J.K Rowling, Joanne K,Rowling, Joanne K.Rowling과 같이 다른 방식으로 표기가 되어있는 경우가 있다
""")

st.write("""
##### 도서별 이용횟수와 평균 평점
도서의 정보 및 이용 횟수와 평균 평점 추가한 데이터셋 생성
""")
st.write('')
st.write('')

st.write("""
##### ✔ 유저들이 가장 많이 이용한 상위 10개 도서

""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_user = pd.read_csv('data/popbooks.csv')

fig1, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='N_ratings', y='Book-Title', data=df_user,palette='Set1')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Top10 Books most read by users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig1)
 

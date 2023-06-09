import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('👨‍📝고객분석')


st.sidebar.markdown("""
    ## 고객 분석
    - [part 1. 나이별 분석](#part-1-age-analysis)
    - [part 2. 지역별 분석](#part-2-location-analysis)
    - [part 3. 유저별 분석](#part-3-user-analysis)
""")
st.write('')
st.write("""
- 도서평점을 부여한 고객들의 특성 및 취향에 대한 분석으로 도서 평점 데이터를 활용하여 고객들의 취향이나 평점 패턴 등을 분석하고 성별, 연령, 지역등 고객의 특성에 따른 평점 차이를 파악할 수 있다. 이를 통해 어떤 책이 어떤 특성을 가진 고객들이 어떤 책을 선호하는지를 파악할 수 있다. 
""")
st.write('')
st.write('')
st.write("""
### Dataset
""")
df_train = pd.read_csv('data/Country.csv')
st.dataframe(df_train)

st.write('')
st.write('')

js = "window.scrollTo(0, document.getElementById('part-1-age-analysis').offsetTop);"

    
st.markdown("<h3 id='part-1-age-analysis'>✅Part 1. 나이별 분석</h3>", unsafe_allow_html=True)

st.write("""
#### DATA 전처리

- 의견1) 0세는 상위1% 값이 15세로 대체. 모두 하위 4%와 3% 구간 사이에서 비교적 급격한 나이 변화가 일어났으므로 급격한 나이변화가 일어나는 구간부터는 모두 이상치로 판단, 따라서 하위4% 이하인 80세 이상은 모두 80세로 대체
- 의견2) 상위 1%인 0-15세를 모두 15세로 대체하며, 하위1%에 해당하는 67세-244세는 모두 67세로 대체
- 의견3) 나이별 사분위수 와 threshold사용

-> 모델 예측점수 결과가 가장 좋았던 의견 1)을 사용하기로 함

""")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('data/Country.csv')

# 히스토그램 그리기
fig4 = plt.figure()
plt.hist(data=df, x='Age', bins=30, rwidth=0.8)
plt.title('Age Distribution') # 그래프 제목 설정
plt.xlabel('Age') # x축 레이블 설정
plt.ylabel('Count') # y축 레이블 설정

# 그래프 표시하기
st.pyplot(fig4)

st.write('')
st.write('')
st.write('')

js = "window.scrollTo(0, document.getElementById('part-2-location-analysis').offsetTop);"
  
st.markdown("<h3 id='part-2-location-analysis'>✅Part 2. 지역별 분석</h3>", unsafe_allow_html=True)

st.write("""
#### DATA 전처리

- Location(city, state, country) 로 구성.
- 해당 데이터는 사용자가 자유롭게 지역을 기입하는 방식으로 구성되어 있어 아래와 같이 국가정보 파악이 힘든 데이터가 있음을 발견(이상값과 결측값 수정 및 제거)
- 국가 정보만 있는 새로운 열 생성(국가명(Country)을 ISO-3166-1 alpha-3 국가 코드로 변환)
- 주 정보만 있는 새로운 열 생성
""")

st.write("""
   
     
""")

st.write("""
##### ✔ 상위 10개 나라별 평점 수
도서 이용량이 많은 나라는 미국이 압도적으로 가장 많으며 캐나다, 영국, 독일, 호주 등으로 분포되어있다.
- USA = 미국
- CAN = 캐나다
- GBR = 영국
- DEU = 독일
- AUS = 호주
- ESP = 스페인
- FRA = 프랑스
- PRT = 포르투갈
- NZL = 뉴질랜드
- MYS = 말레이시아
""")

st.write('')
st.write('')
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_location = pd.read_csv('data/rating_count.csv')

fig3, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='index', y='Country', data=df_location, ax=ax)
ax.set_title('Number of ratings by country') # 그래프 제목 설정

# 그래프 표시하기
st.pyplot(fig3)


st.write("""
##### ✔ 상위 10개 나라별 평균 평점 수 
나라별 도서평균평점을 가장 높게 준 나라는 순서대로 우간다이며 가봉 리투아니아 과테말라가 뒤를 잇는다.
- UGA = 우간다
- GAB = 가봉
- LTU = 리투아니아
- GTM = 과테말라
- MUS = 모리셔스공화국
- VNM = 베트남
- BGD = 방글라데스
- GNB = 기니비사우
- AND = 안다우스
- BRN = 브루나이
""")

st.write('')
st.write('')


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_avg = pd.read_csv('data/avg_country.csv')

fig2, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Country', y='Rating-Per-Count', data=df_avg, ax=ax)
ax.set_title('Average rating by country') # 그래프 제목 설정

# 그래프 표시하기
st.pyplot(fig2)
st.write('')
st.write('')
st.write('')

js = "window.scrollTo(0, document.getElementById('part-3-user-analysis').offsetTop);"

st.markdown("<h3 id='part-3-user-analysi'>✅Part 3. 유저별 분석</h3>", unsafe_allow_html=True)
st.write('')
st.write('')

st.write("""
##### ✔ 상위 10위 유저별 최대 평점 수 
- USER_56601이 11143번의 평점 수를 기록했다.
- 그 뒤로 USER_54865, 52453, 73501 등이 높은 순위를 기록했다.
""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_user = pd.read_csv('data/users.csv')

fig1, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='N_ratings', y='User-ID', data=df_user,palette='Set1')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Maximum number of ratings for top 10 users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig1)


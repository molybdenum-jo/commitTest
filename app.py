import streamlit as st
import pandas as pd
import numpy as np

st.header('도서 평점 예측을 통한 도서 추천 시스템')
st.write(""" 
분석 주제 : 제2회 코스포 x 데이콘 도서 추천 알고리즘 AI 경진대회
프로젝트 기간 : 2023.04.26 - 2023.05.09
""")
st.subheader('AI school 8기 Final_Project')

st.write(""" 
## Team Report
- GITHUB : https://github.com/sangminkingg/Book-recommendation
- EDA
- NOTION : https://www.notion.so/likelion-aischool/5b12b950b0de448dbc03ec1150d12c01?pvs=4
- DASHBOARD

## Team structure
""")

df = pd.DataFrame({
    '역할':['공공 데이터 적용|n최종 보고서 작성|nppt정리',
           '모델 개발 및 예측 점수 선별|n대시 보드 구축 및 배포',
           '발표|n모델 개발 및 개선'
           ,'EDA 인사이트|n데이터 전처리']
    }, index=pd.Index(data=['김상민','조수연','강다현','사공도경'], name='이름'))

st.dataframe(df)

st.write(""" 
## Insight
""")

st.write(""" 
## 프로젝트 배경

### 넷플릭스처럼 초등학생에게 알고리즘으로 읽을 책을 추천해준다.
최근 유튜브나 넷플릭스처럼 사용자 기반의 인공지능(AI)의 발전으로 고객의 데이터를 통한 AI 추천 알고리즘을 활용하여 독서 성향에 맞게 실시간으로 추천해줌으로써 독서에 대한 관심과 새로운 분야의 분야의 책에 대한 관심도 넓혀갈 수 있다.

### 도서추천 알고리즘의 장점
1. 개인 맞춤형 추천 : 사용자의 독서기록, 검색어, 평점 등을 분석하여 그들의 취향을 파악하여 맞춤형 추천을 제공한다. 이로써 사용자는 자신이 관심있는 도서책을 쉽게 찾을 수 있다.
2. 다양한 도서책 추천 : 사용자가 이전에 읽어본 도서책과는 다른 도서책도 추천해준다. 이렇게 함으로써 사용자는 다양한 장르나 분야의 도서책을 발견할 수 있다.
3. 비용절감 : 개인별 추천 서비스를 제공할 수 있으므로 책 추천에 따른 추가적인 비용을 지불하지 않아도 된다.
4. 빠른 속도 : 수 많은 도서책을 분석하고 맞춤형 추천을 제공하는 작업을 자동화하여 빠른 속도로 추천 결과를 제공할 수 있다.
5. 개인 정보 보호 : 사용자의 개인정보를 분석하기 때문에 개인 정보 보호에 대한 문제가 제기 될 수 있으나 적절한 보안 절차와 규제를 따르면서도 개인 맞춤형 추천 서비스를 제공할 수 있다.
    
### 프로젝트의 활용 방안
1. 온라인 서점에서 추천 도서 제공: 사용자의 구매 이력과 검색 이력 등을 기반으로, 추천 도서를 제공하여 사용자들이 더 많은 도서를 구매하고, 온라인 서점의 매출을 증대시킬 수 있습니다.
2. 도서관에서의 도서 대출: 도서관에서는 사용자의 대출 이력과 관심 분야를 기반으로, 추천 도서를 제공하여 사용자들이 더 많은 도서를 대출하고, 도서관의 이용률을 높일 수 있습니다.
3. 출판사에서의 마케팅: 도서 추천 알고리즘을 사용하여, 특정 장르나 특정 저자의 도서에 대한 사용자들의 선호도를 파악할 수 있습니다. 이를 활용하여 출판사에서는 마케팅 활동을 전개할 수 있습니다.
4. 학술 정보 제공: 학술 분야에서도 도서 추천 알고리즘을 활용하여, 논문, 연구 보고서 등의 정보를 추천할 수 있습니다. 이를 활용하여 연구자들이 더 다양한 정보를 수집하고, 연구의 질을 향상시킬 수 있습니다.
""")
# 사이드바 메뉴 생성
menu = ["Home", "About", "Contact"]

# 페이지 선택
choice = st.sidebar.selectbox("Select an option", menu)

# 각 페이지 내용 작성
if choice == "Home":
    st.title("Home Page")
    st.write("This is the Home page.")

elif choice == "About":
    st.title("About Page")
    st.write("This is the About page.")

else:
    st.title("Contact Page")
    st.write("This is the Contact page.")

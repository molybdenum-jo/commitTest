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
- GITHUB
- EDA
- NOTION
- DASHBOARD

## Team structure
""")

df = pd.DataFrame({
    '역할':['공공 데이터 적용 최종 보고서 작성 ppt정리',
           '모델 개발 및 예측 점수 선별 대시 보드 구축 및 배포',
           '발표 모델 개발 및 개선','EDA 인사이트 데이터 전처리']
    }, index=pd.Index(data=['김상민','조수연','강다현','사공도경'], name='이름'))

st.dataframe(df)



st.write("""
## 고객 분석
1. 나이별 평점 비교
2. 지역별 평점 비교

## 출판사 분석
1. 책 타이틀
2. 작가별
3. 도서출판일
4. 출판사별

## 도서평점예측을 통한 도서추천시스템
1. 협업필터링 기반의 추천시스템
2. 콘텐츠 기반의 추천시스템
3. 행렬 인수분해 기반의 추천시스템
4. 딥 러닝 모델 기반의 추천시스템
5. 앙상블 기법을 사용한 추천시스템
6. 하이퍼파라미터 최적화를 통한 추천시스템
""")

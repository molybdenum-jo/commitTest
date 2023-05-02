import streamlit as st
import pandas as pd
import numpy as np

st.title('도서 추천시스템')
st.title('도서평점 예측을 통한 도서 추천시스템')
st.sidebar.title('고객분석

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
                 
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

import streamlit as st
import pandas as pd
import numpy as np


st.header('Part1. 연령별 평점 비교')
st.write("""
### DATA 전처리
- 0세 => 15세
- 100세 이상 => 67세

### Dataset
""")
uploaded_file = st.file_uploader("파일 업로드", type=["csv", "txt"])
if uploaded_file is not None:
    # 파일을 파이썬 객체로 읽어들임
    df = pd.read_csv(uploaded_file)
    st.write(df)

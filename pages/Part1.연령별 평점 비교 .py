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
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    # 업로드한 파일을 데이터프레임으로 변환
    df = pd.read_csv(uploaded_file)

    # 새로운 파일로 저장
    df.to_csv("new_file.csv", index=False)
    st.success("File saved successfully")

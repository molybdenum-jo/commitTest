import streamlit as st
import pandas as pd
import numpy as np


st.header('고객분석')
st.sidebar.title('고객분석')

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
from PIL import Image

image = Image.open('image.jpg')
st.image(image, caption='Image Caption')


st.write(""" 
### part 2. 지역별 분석
""")


st.write(""" 
### part 3. 유저 분석 
""")

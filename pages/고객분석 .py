import streamlit as st
import pandas as pd
import numpy as np


st.header('고객')
st.sidebar.title('Part1. 연령별 평점 비교')
st.write("""
### DATA 전처리
- 0세 => 15세
- 100세 이상 => 67세

### Dataset
""")

import streamlit as st
import pandas as pd
import numpy as np


st.header('고객분석')
with st.sidebar:
  choose = option_menu("고객분석",["part 1. 나이별 분석","part 2. 지역별 분석","part 3. 유저 분석 "],
                       icons=['house', 'camera fill', 'kanban'],
                       menu_icon="app-indicator", default_index=0)
st.write("""
### DATA 전처리
- 0세 => 15세
- 100세 이상 => 67세

### Dataset
""")

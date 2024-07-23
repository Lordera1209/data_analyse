#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Version  : 3.11
# @Author   : Lordera
# @Datetime : 2024/7/22 上午10:10
# @Project  : stream_lit
# @File     : demo2.py

import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header("资料信息分析")

df = pd.read_csv('.data/data.csv')

report = ProfileReport(df, title='My Data')
report.to_file("my_report.html")
st_profile_report(report)

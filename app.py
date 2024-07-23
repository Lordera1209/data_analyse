#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Version  : 3.11
# @Author   : Lordera
# @Datetime : 2024/7/22 上午10:10
# @Project  : stream_lit
# @File     : demo2.py

import streamlit as st
import pandas as pd
# 原为 import pandas_profiling, 新版本中已更新为ydata_profiling
from ydata_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report

st.header("资料信息分析")

df = pd.read_csv('./data.csv')

# 进行各方面数据分析，生成详细的HTML报告
# pr = df.profile_report()
report = ProfileReport(df)
# 将生成的报告展示在Streamlit应用程序中
st_profile_report(report)

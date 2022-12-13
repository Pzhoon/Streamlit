import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title(
    """강원랜드 무인AI커피머신 판매량"""
    )
st.subheader(
    "12월 총 판매량"
)

df = pd.read_csv('./gangwon/gangwon.csv', encoding='cp949')
gangwon1225 = df.iloc[5000:5020]
gangwon12 = df.iloc[4588:5129]

fig1 = px.histogram(gangwon12, x="상품명", y='판매수량',title='12월 판매량' )
st.plotly_chart(fig1)
fig2 = px.histogram(gangwon1225, x="상품명", y='판매수량',title='크리스마스 판매량' )
st.rugplot(fig2)


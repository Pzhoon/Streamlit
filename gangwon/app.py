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

# st.sidebar.header('Menu')
# name = st.sidebar.selectbox('분기별 판매량', ['전체','1분기','2분기','3분기','4분기'])

df = pd.read_csv('./gangwon/gangwon.csv', encoding='cp949')
gangwon1225 = df.iloc[5000:5020]
gangwon12 = df.iloc[4588:5129]
first = df.iloc[:627]
second = df.iloc[627:1976]
third = df.iloc[1976:3518]
forth = df.iloc[3518:]


fig1 = px.histogram(gangwon12, x="상품명", y='판매수량',title='12월 판매량')
st.plotly_chart(fig1)
#fig1 = px.data.gapminder()
#fig = px.line(df, x="영업일자", y="판매수량", title='12월 판매량')
fig1 = px.line(gangwon12, x="영업일자", y='판매수량',title='12월 판매량')
st.plotly_chart(fig1)
fig2 = px.histogram(gangwon1225, x="상품명", y='판매수량',title='크리스마스 판매량')
st.plotly_chart(fig2)
# fig.show()

# 판매량 베스트3
st.header(
    "Best 3"
)
col1, col2, col3 = st.columns(3)
with col1:
   st.subheader("1.아메리카노 2103잔")
   st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

with col2:
   st.subheader("2.바닐라라떼 389잔")
   st.image("data:image/jpeg;base64,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")

with col3:
	st.subheader("3.카페라떼 383잔")
	st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")

#판매량 워스트3
st.header(
    "Worst 3"
)
col4, col5, col6 = st.columns(3)
with col4:
   st.subheader("1.그린티라떼 64잔")
   st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt0MkgkF0fpSWfxoxWky90vkS7z5tQm4zDhsNyo4Yy1fE6ZWBVQ7zjdcCpk2AcVrBRtcc&usqp=CAU")

with col5:
   st.subheader("2.카페모카 119잔")
   st.image("https://mblogthumb-phinf.pstatic.net/MjAxOTA2MTBfMTk4/MDAxNTYwMTQ1OTQ2NzY5.dsi0jVneKpvjZExfrwfOBrcVBXPv4-JKHV0NJPUCLbUg.kfRkTjZCWCh8zxRlGrMd3jdEEI6iKSJCbpWVgs4lnx0g.JPEG.ydc0923/SE-fd1c88d8-9dfe-4742-a532-fe2bf9b61e5e.jpg?type=w800")
with col6:
	st.subheader("3.흑당라떼 120잔")
	st.image("https://mblogthumb-phinf.pstatic.net/MjAxOTA4MjBfNDgg/MDAxNTY2MjgyMzQyNTcz.S-J8_RU-AwoHJEo0MH6r1vWxwXRhtJvwg1_yezGf-tQg.DG6VIs49j9F-h_5yVDYoS9fLvx1VCkjeAgTr5GYM3uog.PNG.qonemkt/SE-eae85b63-7689-4f2c-a653-9db114c0f2ec.png?type=w800")

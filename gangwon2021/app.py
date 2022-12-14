import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title(
    """강원랜드 인공지능 AI 빅데이터 기반 Data Analysis & Data Visualization Project"""
    )
st.write('&nbsp;')
st.write('&nbsp;')
st.write('&nbsp;')

st.subheader("""
강원랜드_호텔 인공지능 무인카페 이용현황
""")

def main() :

    cof = ['CHOICE','아메리카노','카페라떼','흑당라떼','초코라떼','스위티자몽','바닐라라떼','아이스티','자두주스','청포도주스','카페모카','카푸치노','그린티라떼']
    choice = st.selectbox('귀하가 선호하는 카페 음료는 무엇입니까?', cof)

    if choice == cof[1] :
        st.balloons()
        st.write("# 당신이 고른 음료는 첫번째로 많이 팔렸어요 ")
    elif choice == cof[2] :
        st.balloons()
        st.write("# 당신이 고른 음료는 두번째로 많이 팔렸어요")
    elif choice == cof[3] :
        st.snow()
        st.write("# 당신이 고른 음료는 여덟번째로 많이 팔렸어요.")
    elif choice == cof[4] :
        st.balloons()
        st.write("# 당신이 고른 음료는 다섯번째로 많이 팔렸어요.")
    elif choice == cof[5] :
        st.balloons()
        st.write("# 당신이 고른 음료는 여섯번째로 많이 팔렸어요.")
    elif choice == cof[6] :
        st.balloons()
        st.write("# 당신이 고른 음료는 세번째로 많이 팔렸어요.")
    elif choice == cof[7] :
        st.snow()
        st.write("# 당신이 고른 음료는 아홉번째로 많이 팔렸어요.")
    elif choice == cof[8] :
        st.snow()
        st.write("# 당신이 고른 음료는 열번째로 많이 팔렸어요.")
    elif choice == cof[9] :
        st.balloons()
        st.write("# 당신이 고른 음료는 네번째로 많이 팔렸어요.")  
    elif choice == cof[10] :
        st.snow()
        st.write("# 당신이 고른 음료는 일곱번째로 많이 팔렸어요.")
    elif choice == cof[11] :
        st.snow()
        st.write("# 당신이 고른 음료는 열한번째로 많이 팔렸어요.")
    elif choice == cof[-1] :
        st.snow()
        st.write("# 당신이 고른 음료는 열두번째로 많이 팔렸어요.")


if __name__ == '__main__' :
    main()

def main():
    df = pd.read_csv('./gangwon/gangwon.csv', encoding='cp949')
    if st.checkbox('원본 데이터 보기'):
        st.subheader('Raw data')
        st.write(df)

if __name__ == '__main__' :
    main()

st.sidebar.header('Menu')
name = st.sidebar.selectbox('분기별 판매량', ['종류를 선택해주세요','1분기','2분기','3분기','4분기','전체'])

df = pd.read_csv('./gangwon/gangwon.csv', encoding='cp949')
gangwon1225 = df.iloc[5000:5020]
gangwon12 = df.iloc[4588:5129]
first = df.iloc[:627]
second = df.iloc[627:1976]
third = df.iloc[1976:3518]
forth = df.iloc[3518:]

if name == '1분기':
    total_sum1 = first['판매수량'].sum()
    st.subheader(f"1분기 총 판매량 {total_sum1}잔 입니다")
    fig_first = px.histogram(first, x="상품명", y='판매수량',title='강원랜드 무인 카페 1분기 음료 판매량' )

    st.plotly_chart(fig_first)

    sample1 = first[first['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 1분기의 승자는 HOT 입니다.")
    fug1 = px.histogram(sample1, x="상품명", y='판매수량')
    st.plotly_chart(fug1)


    st.write("## BEST 3")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("1.아메리카노 HOT 995잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col2:
        st.subheader("2.아메리카노 ICE 753잔")
        st.image("https://img.freepik.com/premium-photo/iced-americano-coffee-glass-bar-cafe_213396-399.jpg?w=2000")
    with col3:
	    st.subheader("3.카페라떼 HOT 204잔")
	    st.image("https://www.the-cup.co.kr/data/editor/1902/thumb-687c8d0c78d329e0c637df3050b1fd20_1550129060_1108_920x843.jpg")


    st.write("## WORST 3")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.subheader("1.그린티라떼 ICE 19잔")
        st.image("https://t1.daumcdn.net/cfile/tistory/997CD3375BB7413D26")

    with col5:
        st.subheader("2.그린티라떼 HOT 23잔")
        st.image("https://cdn.crowdpic.net/detail-thumb/thumb_d_60500265FA5D54A4A9986162EAD3CD9F.jpg")

    with col6:
	    st.subheader("3.흑당라떼 HOT 28잔")
	    st.image("https://www.the-cup.co.kr/data/file/cafe_peple/1028825330_r2YHJtvM_f5411b42f6c8b4072214153368ce717ce340b578.jpg")

elif name == '2분기':

    total_sum2 = second['판매수량'].sum()
    st.subheader(f"2분기 총 판매량 {total_sum2}잔 입니다.")

    fig_second = px.histogram(second, x="상품명", y='판매수량',title='강원랜드 무인 카페 2분기 음료 판매량' )

    st.plotly_chart(fig_second)

    sample2 = second[second['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 2분기의 승자는 HOT 입니다.")
    fug2 = px.histogram(sample2, x="상품명", y='판매수량')
    st.plotly_chart(fug2)

    st.write("## BEST 3")
    col7, col8, col9 = st.columns(3)
    with col7:
        st.subheader("1.아메리카노 HOT 2020잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col8:
        st.subheader("2.아메리카노 ICE 1937잔")
        st.image("https://img.freepik.com/premium-photo/iced-americano-coffee-glass-bar-cafe_213396-399.jpg?w=2000")

    with col9:
	    st.subheader("3.청포도주스 ICE 403잔")
	    st.image("https://www.qone.co.kr/Upload/Recipe/Recipe_202131594130.jpg")
    
    st.write("## WORST 3")
    col10, col11, col12 = st.columns(3)
    with col10:
        st.subheader("1.그린티라떼 HOT 51잔")
        st.image("https://cdn.crowdpic.net/detail-thumb/thumb_d_60500265FA5D54A4A9986162EAD3CD9F.jpg")

    with col11:
        st.subheader("2.그린티라떼 ICE 57잔")
        st.image("https://t1.daumcdn.net/cfile/tistory/997CD3375BB7413D26")

    with col12:
	    st.subheader("3.스위티자몽 HOT 63잔")
	    st.image("https://mblogthumb-phinf.pstatic.net/MjAxNzA3MTBfNjEg/MDAxNDk5Njk1ODE0NDQ5.c0_66V5veY9rrg6HDVjRBfFm4IuX4Lcg5QhWDTt_bKEg.GM-vsSH0Ua1RG6GcBps50qvh2D6aDkHk9wFgIicIpywg.JPEG.florencenightingale/%EC%9E%90%EB%AA%BD%EC%A3%BC%EC%8A%A4.jpg?type=w800")

elif name == '3분기':

    total_sum3 = third['판매수량'].sum()
    st.subheader(f"3분기 총 판매량 {total_sum3}잔 입니다.") 
    
    fig_third = px.histogram(third, x="상품명", y='판매수량',title='강원랜드 무인 카페 3분기 음료 판매량' )

    st.plotly_chart(fig_third)

    sample3 = third[third['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 3분기의 승자는 ICE 입니다.")
    fug3 = px.histogram(sample3, x="상품명", y='판매수량')
    st.plotly_chart(fug3)

    st.write("## BEST 3")
    col13, col14, col15 = st.columns(3)
    with col13:
        st.subheader("1.아메리카노 ICE 3433잔")
        st.image("https://img.freepik.com/premium-photo/iced-americano-coffee-glass-bar-cafe_213396-399.jpg?w=2000")

    with col14:
        st.subheader("2.아메리카노 HOT 2290잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col15:
	    st.subheader("3.청포도주스 ICE 636잔")
	    st.image("https://www.qone.co.kr/Upload/Recipe/Recipe_202131594130.jpg")
    
    st.write("## WORST 3")
    col16, col17, col18 = st.columns(3)
    with col16:
        st.subheader("1.그린티라떼 HOT 66잔")
        st.image("https://cdn.crowdpic.net/detail-thumb/thumb_d_60500265FA5D54A4A9986162EAD3CD9F.jpg")

    with col17:
        st.subheader("2.흑당라떼 HOT 104잔")
        st.image("https://www.the-cup.co.kr/data/file/cafe_peple/1028825330_r2YHJtvM_f5411b42f6c8b4072214153368ce717ce340b578.jpg")

    with col18:
	    st.subheader("3.카푸치노 HOT 110잔")
	    st.image("http://www.beantobean.com/web/upload/NNEditor/20160513/ECB9B4ED91B8ECB998EB85B8.jpg")
    
elif name == '4분기':

    total_sum4 = forth['판매수량'].sum()
    st.subheader(f"4분기 총 판매량 {total_sum4}잔 입니다.")

    fig_forth = px.histogram(forth, x="상품명", y='판매수량',title='강원랜드 무인 카페 4분기 음료 판매량' )

    st.plotly_chart(fig_forth)  

    sample4 = forth[forth['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 4분기의 승자는 HOT 입니다.")
    
    fug4 = px.histogram(sample4, x="상품명", y='판매수량')
    st.plotly_chart(fug4)
    st.write("## BEST 3")
    col19, col20, col21 = st.columns(3)
    with col19:
        st.subheader("1.아메리카노 HOT 3772잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col20:
        st.subheader("2.아메리카노 ICE 3179잔")
        st.image("https://img.freepik.com/premium-photo/iced-americano-coffee-glass-bar-cafe_213396-399.jpg?w=2000")

    with col21:
	    st.subheader("3.바닐라라떼 HOT 730잔")
	    st.image("data:image/jpeg;base64,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")
    
    st.write("## WORST 3")
    col22, col23, col24 = st.columns(3)
    with col22:
        st.subheader("1.그린티라떼 HOT 106잔")
        st.image("https://cdn.crowdpic.net/detail-thumb/thumb_d_60500265FA5D54A4A9986162EAD3CD9F.jpg")

    with col23:
        st.subheader("2.그린티라떼 ICE 106잔")
        st.image("https://t1.daumcdn.net/cfile/tistory/997CD3375BB7413D26")

    with col24:
	    st.subheader("3.카페모카 ICE 139잔")
	    st.image("http://gdimg.gmarket.co.kr/971781522/still/600?ver=0")



elif name == '전체':
    total_sum5 = df['판매수량'].sum()
    st.subheader(f"21년 총 판매량 {total_sum5}잔 입니다.")

    fig_all = px.histogram(df, x="상품명", y='판매수량',title='강원랜드 무인 카페 21년 총 음료 판매량' )

    st.plotly_chart(fig_all)

    sample5 = df[df['상품명'].str.contains('아메리카노')]

    st.write("## HOT vs ICE")
    st.write("### 21년의 승자는 ICE 입니다.")


    fug5 = px.histogram(sample5, x="상품명", y='판매수량')
    st.plotly_chart(fug5)

    st.write("## BEST 3")
    col25, col26, col27 = st.columns(3)
    with col25:
        st.subheader("1.아메리카노 ICE 9302잔")
        st.image("https://img.freepik.com/premium-photo/iced-americano-coffee-glass-bar-cafe_213396-399.jpg?w=2000")

    with col26:
        st.subheader("2.아메리카노 HOT 9077잔")
        st.image("https://health.chosun.com/site/data/img_dir/2022/05/11/2022051101651_0.jpg")

    with col27:
	    st.subheader("3.청포도주스 ICE 1886잔")
	    st.image("https://www.qone.co.kr/Upload/Recipe/Recipe_202131594130.jpg")
    
    st.write("## WORST 3")
    col28, col29, col30 = st.columns(3)
    with col28:
        st.subheader("1.그린티라떼 HOT 246잔")
        st.image("https://cdn.crowdpic.net/detail-thumb/thumb_d_60500265FA5D54A4A9986162EAD3CD9F.jpg")

    with col29:
        st.subheader("2.그린티라떼 ICE 329잔")
        st.image("https://t1.daumcdn.net/cfile/tistory/997CD3375BB7413D26")

    with col30:
	    st.subheader("3.흑당라떼 HOT 410잔")
	    st.image("https://www.the-cup.co.kr/data/file/cafe_peple/1028825330_r2YHJtvM_f5411b42f6c8b4072214153368ce717ce340b578.jpg")

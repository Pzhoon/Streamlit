# streamlit 라이브러리 호출
import streamlit as st
import numpy as np

# st.write() 마크다운
st.title("조추첨 페이지")
st.header("게임을 시작하지")
# https://docs.streamlit.io/library/cheatsheet

# 추첨 대상인 13명의 이름을 넣을 수 있는 text_input
# 3 x 4 (row, col)
# 열을 배치하는 메소드
columns = st.columns(4)
# col1, col2, col3, col4
for idx, col in enumerate(columns):
    # col.text_text_input(f"추첨 대상자 {idx+1}", key=idx)
    for idx2 in range(4):
        # key가 겹치면 안 됨
        col.text_input(f"조 추첨 대상 {idx+1 + idx2 * 4}", key=f"{idx+1 + idx2 * 4}")
st.text_input("추첨 대상자")
# 13명이 소속될 조 이름을 넣을 위치

# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽

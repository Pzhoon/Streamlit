# streamlit 라이브러리 호출
import streamlit as st
import numpy as np
import pandas as pd

# st.write() 마크다운
st.title("조추첨 페이지")
st.header("게임을 시작하지")
# https://docs.streamlit.io/library/cheatsheet
st.image("https://images.unsplash.com/photo-1570303345338-e1f0eddf4946?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGljZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60")
#st.image("./lucky/xx.jpg")

# 추첨 대상인 13명의 이름을 넣을 수 있는 text_input
# 3 x 4 (row, col)
# 열을 배치하는 메소드

tabs = st.tabs(["참가자", "조"])

#0번째 탭에 컬럼(열)을 넣겠다
columns = tabs[0].columns(4)
# col1, col2, col3, col4
for idx, col in enumerate(columns):
    # col.text_text_input(f"추첨 대상자 {idx+1}", key=idx)
    for idx2 in range(4):
        # key가 겹치면 안 됨
        col.text_input(f"조 추첨 대상 {idx+1 + idx2 * 4}", key=f"n{idx+1 + idx2 * 4}")

columns2 = tabs[1].columns(4)
# col1, col2, col3, col4
for idx, col in enumerate(columns2):
    # col.text_text_input(f"추첨 대상자 {idx+1}", key=idx)
    for idx2 in range(4):
        # key가 겹치면 안 됨
        col.text_input(f"조 추첨 대상 {idx+1 + idx2 * 4}", key=f"g{idx+1 + idx2 * 4}")
#추첨버튼
if st.button('추첨 시작'):
ss = pd.Series(st.session_state)
# st.write(ss)

ss2 = ss[ss.ne("")]
st.write(ss2)
n_idx = ss2.index.str.contains("n")
n_data = ss2[n_idx]
# st.write(n_data)

g_idx - ss2.index.str.sontains("g")
g_data = ss2[g_idx]
# st.write(g_data)

# n_data를 섞어줄 것임 (비복원으로)
n_rd = np.random.choice(n_data, len(n_data), replace=False)
# st.write(n_rd)
g_rd = np.random.choice(g_data, len(g_data), replace=False)
# st.write(g_rd)
# 2. df 형태로 정리
# 13개의 짝을 지어서 표시해줄 그래픽
df = pd.DataFrame({
    "추첨 대상자 이름": n_rd,
    "조 이름": g_rd,
})
# st.balloons()
st.snow()
st.write(df)

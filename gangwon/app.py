import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title(
    """강원랜드 무인커피 판매량"""
    )
st.subheader(
    ""12월 총 판매량""
)
# gangwon = sns.load_dataset('gangwon')
df = pd.read_csv('./gangwon/gangwon.csv')

fig = plt.figure(figsize=(6, 3))
gangwon['영업일자'] = 
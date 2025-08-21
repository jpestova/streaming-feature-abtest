import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Streaming Feature AB Test Dashboard")

# Загружаем данные
df = pd.read_csv("../data/events.csv", parse_dates=["timestamp"])

# DAU
df['date'] = df['timestamp'].dt.date
dau = df.groupby('date')['user_id'].nunique()
st.line_chart(dau)

# Конверсия в подписку по группам
conversion = df.groupby('ab_group')['subscribed'].mean()
st.bar_chart(conversion)

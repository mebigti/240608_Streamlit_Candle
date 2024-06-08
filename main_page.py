import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
# st.image('umbro.png', caption='sunrise') 왜 이미지가 로딩되지 않는지 알기 어려움 일단은 마크다운 방식의 경로 및 링크 생성이 동일한 기능을 수행하므로 이를 따르도록 함
st.title("CAT")
st.image("umboy.png")

# Load the CSV file
df = pd.read_csv('AAPL.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Streamlit app
st.title('AAPL Stock Data')

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

fig.update_layout(title='AAPL Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Price',
                  xaxis_rangeslider_visible=False)

# Display chart
st.plotly_chart(fig)

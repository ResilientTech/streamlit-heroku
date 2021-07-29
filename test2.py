import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
## Stock price app

""")

tkSymbol = 'GOOGL'
tkData = yf.Ticker(tkSymbol)
tickerDf = tkData.history(period='1d', start='2021-07-01', end='2021-07-15')

st.write("""
### Closing **price** of Google stock 
### 2021 July 1-15 

""")
    
st.line_chart(tickerDf.Close)

st.write("""
### Trading volume of Google stock
### 2021 July 1-15

""") 
st.line_chart(tickerDf.Volume)

st.write("""
### Opening price of ***Google*** stock 

""")
         
st.bar_chart(tickerDf.Open)




    


import yfinance as yf
import streamlit as st

#bRead the Redme file to know more about the tools have been used

st.write("""
# Easy-Peasy Stock Price App
Stock closing price and volume of Apple!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#the ticker symbol

tickerSymbol = 'AAPL'
"""
A ticker symbol or stock symbol is an abbreviation
used to uniquely identify publicly traded shares of a particular stock on a particular stock market.
"""
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-5-04')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
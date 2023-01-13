import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """
    # Simple Stock Price App

    Shown are the stock **closing price** and **volume** of Google!
    """
)

# define the ticker symbol
tickerSymbol = 'GOOGL'

# define data on this ticker 
tickerData = yf.Ticker(tickerSymbol)

# get the historical price for this ticker
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

# Close price
st.write("""## Close Price""")
st.line_chart(tickerDf.Close)

# Volume price
st.write("""## Close Price""")
st.line_chart(tickerDf.Volume)
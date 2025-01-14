import streamlit as st
import pandas as pd
import yfinance as yf 
import datetime

st.title("Stock Market App")

st.write("This is my hope of getting hike.")


start_date = st.date_input("Please enter Start Date", datetime.date(2019, 1, 1))
end_date = st.date_input("Please enter End Date", datetime.date(2021, 1, 1))

ticker_symbol = st.text_input("Please enter the ticker symbol", "AAPL")

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)
st.dataframe(ticker_df)

st.write(
    '''
    ## Daily Closing Price Chart
    '''
)

st.line_chart(ticker_df['Close'])


col1, col2= st.columns(2)

# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")


with col1:
    st.write(
        '''
        ## Daily Closing Price Chart
        '''
    )
    st.line_chart(ticker_df['Close'])

with col2:
    st.write(
        '''
            ## Daily Volume Price Chart
        '''
    )
    st.line_chart(ticker_df['Volume'])






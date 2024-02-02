# raw package
import numpy as np  # required dependency for yfinance
import pandas as pd # required dependency for yfinance
import tkinter as tk
#stock_data source
import yfinance as yf
#stock_data visualization
#import plotly.graph_objs as grobj


def total_return(ticker):

    user_ticker = ticker
    total_shares = float(input("Enter the amount of shares you hold: "))
    avg_cost = float(input("Enter the average cost of your shares: "))

    stock_data = yf.Ticker(user_ticker)

    initial_investment = total_shares * avg_cost

    current_price = stock_data.info.get('currentPrice', 'price stock_data not found')
    
    shares_need_sold = 0

    print(f"The current price of {user_ticker} is {current_price}")

    if float(current_price) <= avg_cost:
        print("At current market prices you cannot recoup your total investment.")
    else:
        shares_need_sold = round(initial_investment/current_price, 2)
        print(f"At current market prices if you sold {shares_need_sold} shares of {user_ticker} you would reclaim your initial cost.")

total_return(input("Enter the ticker of the stock: ").upper())

# split up the function into smaller parts that work together through multiple function calls


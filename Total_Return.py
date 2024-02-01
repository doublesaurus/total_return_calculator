# raw package
import numpy as np  # required dependency for yfinance
import pandas as pd # required dependency for yfinance
import tkinter as tk
#data source
import yfinance as yf
#data visualization
#import plotly.graph_objs as grobj



user_ticker = input("Enter the ticker of the stock: ")
stock_ticker1 = user_ticker.upper()

data = yf.Ticker(stock_ticker1)


user_shares = float(input("Enter the amount of shares you hold: "))
user_avg_cost = float(input("Enter the average cost of your shares: "))

initial_investment = user_shares * user_avg_cost

current_price = data.info.get('currentPrice', 'price data not found')
shares_need_sold = 0

print(f"The current price of {stock_ticker1} is {current_price}")

if float(current_price) <= user_avg_cost:
    print("At current market prices you cannot recoup your total investment.")
else:
    shares_need_sold = initial_investment/current_price
    print(f"At current market prices if you sold {shares_need_sold} of your shares of {stock_ticker1} you would reclaim your initial investment!")




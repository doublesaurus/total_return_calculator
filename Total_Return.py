# raw package
import numpy as np  # required dependency for yfinance
import pandas as pd # required dependency for yfinance
import tkinter as tk
import yfinance as yf # stock data source


def total_return_calculator(ticker):

    total_shares = float(input("Enter the amount of shares you hold: "))
    avg_cost = float(input("Enter the average cost of your shares: "))

    stock_data = yf.Ticker(ticker)    # gets the ticker information from yfinance

    initial_investment = total_shares * avg_cost   

    current_price = stock_data.info.get('currentPrice', 'price stock_data not found')   # retrieves current market price of ticker if it can be found

    shares_to_sell = 0

    print(f"The current price of {ticker} is ${current_price}")

    if float(current_price) < avg_cost:
        print("At current market prices you cannot recoup your total investment.")
        print(f"You are at an unrealized loss of {round(initial_investment - (current_price * total_shares), 2)}")
    else:
        shares_to_sell = round(initial_investment / current_price, 2)
        print(f"At current market prices if you sold {shares_to_sell} shares of {ticker} you would reclaim your initial cost.")
        print(f"This would leave you with {total_shares - shares_to_sell} shares left of {ticker}.")

total_return_calculator(input("Enter the ticker of the stock: ").upper())

# split up the function into smaller parts that work together through multiple function calls


import yfinance as yf

ticker = input("Enter stock symbol: ")
stock = yf.Ticker(ticker)

data = stock.history(period="5d")
print(data[['Close']])

import quandl
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import seaborn as sns
# sns.set()
# tips = sns.load_dataset("tips")
# sns.relplot(x="total_bill", y="tip", col="time",
#             hue="smoker", style="smoker", size="size",
#             data=tips);






# Stock dates we are interested in
start = datetime.datetime(2016, 1, 1)
end = datetime.date.today()

# List the stock ticker names interested in
stocks = ["AAPL"]  # , "MSFT", "NKE", "V"

# Print out the data to figure
Database = {}
for stock in stocks:
    Stock = quandl.get("WIKI/" + stock, start_date=start, end_date=end)

    plt.plot(Stock["Close"], '-', linewidth=1,  label=stock+" Close")
    plt.plot(Stock["Open"], '--', linewidth=1,  label=stock+" Open")
    Database[stock] = pd.DataFrame(Stock)
    # print(df)

#X = Database["AAPL"][1]
#print(X)

#A = pd.DataFrame(Database)



# Figure setting
plt.grid(which='both')
plt.minorticks_on()
plt.legend()
plt.xlabel('Date [Year-Month]')
plt.ylabel('Stock Prices (£)')
plt.show()


import seaborn as sns
sns.set(style="whitegrid")

rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
data = data.rolling(7).mean()

sns.lineplot(data=Stock['Open'], palette="tab10", linewidth=1)

# Access a particular column
# print(Stock.ix[:,0])

from matplotlib.dates import DateFormatter, WeekdayLocator, \
    DayLocator, MONDAY

# from CandleSticks.py import pandas_candlestick_ohlc

# pandas_candlestick_ohlc(Stock, adj=True, stick="month")
# print('Finished')

#apple["Adj. Close"].plot(grid=True)  # Plot the adjusted closing price of AAPL


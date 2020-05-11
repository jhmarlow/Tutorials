from stocker import Stocker

# MSFT is in the WIKI database, which is default
microsoft = Stocker(ticker='MSFT')

# TECHM is in the NSE database
techm = Stocker(ticker='TECHM', exchange='NSE')

Stocker.plot_stock(start_date=None, end_date=None, stats=['Adj. Close'], plot_type='basic')
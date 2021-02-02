import pandas as pd

from src.utils.tools import *
from src.utils.telebot import Telebot
from src.utils.ydownload import StockData
from src.utils.strategies.macd import Macd
from src.utils.charts.charts import Charts

""" Cronometer
from timeit import default_timer as timer
from datetime import timedelta
start = timer()"""  

"""TODO Config - arquivo de config"""
df_tickers_list = pd.read_csv("src/config/tickers.csv", sep=',')
ignore_tickers = ""     #["CSNA3.SA", "USIM5.SA"]
consider_tickers = ["COGN3.SA", "MGLU3.SA"]
period = "1y"
interval = "1wk"
candles = 3
signals_of_revert = ["R+"]

"""Cleanup folders"""
folders_to_cleanup = ["src/charts/html/", "src/charts/jpeg/"]
remove_files_in_folder(folders_to_cleanup)
remove_file("analisys.txt")

photos=[]

for i in range(0, len(df_tickers_list.index)):

    ticker = str("{0}.SA".format(df_tickers_list['tickers'][i]))

    stocks_df = Macd.macd_analisys(
        StockData.get_history(ticker, period, interval), 
        signals_of_revert, 
        candles,
        ticker,
        consider_tickers,
        ignore_tickers
    )

    if isinstance(stocks_df, pd.DataFrame):
        print(ticker)
        filename = Charts.candlestick_chart(ticker, stocks_df, extension_type="jpeg")

        #photos.append(open(filename, 'rb'))

        """ Send reports via Telegram"""
        #if filename is not None:
        #    Telebot().send_photo(filename)

        #init_logging().info("ticker: {}".format(ticker))

#if photos:
#    Telebot().send_photos(photos)

""" Cronometer
end = timer()
print(timedelta(seconds=end-start))"""
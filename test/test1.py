import numpy as np
import pandas as pd
import time
import numpy
import datetime

from pandas import DataFrame
from webdriver_manager.chrome import ChromeDriverManager
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
from selenium import webdriver
browser = webdriver.Chrome(ChromeDriverManager().install())

url = "http://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml"
browser.get(url)
html = browser.page_source

for table in pd.read_html(html):
    table.to_csv('c:/users/Rookie567/desktop/111.csv', index=False, encoding='utf-8-sig')

#table = pd.DataFrame(data=tables)
#print(tables)

#for table in pd.read_html(url,attr={'class':'zw_main3'}):
    #table.to_csv('c:/users/Rookie567/desktop/111.csv')
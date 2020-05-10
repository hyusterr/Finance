#!/bin/python
# -*- coding: cp950 -*-
# this script is for crawling data from https://goodinfo.tw/

import requests
from bs4 import BeautifulSoup

company_id = '2330'

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'referrer': 'https://google.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Pragma': 'no-cache',
        }
response = requests.get('https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=IS_M_QUAR_ACC&STOCK_ID=' + company_id, headers = headers)
response.encoding = 'utf-8'
soup = BeautifulSoup( response.text, 'html.parser' )

# with open( company_id + '-goodinfo.html', 'w', encoding = 'utf-8' ) as f:
#     f.write( response.text )
#     f.close()


data = []
for tr in soup.findAll( 'table' )[-3].findAll('tr', {'bgcolor': 'white'}):
    for td in tr.findAll( 'td' ):
        print( td.text, end='\t' )
    print()

# for d in data:
   #  print( d ) 
 

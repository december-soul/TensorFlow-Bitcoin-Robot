#coding:utf-8
import json
import requests
import matplotlib.pyplot as plt
import time
import datetime
import dateutil.parser
from mpl_toolkits.mplot3d import Axes3D

def get_trades():
    re=requests.get('https://bittrex.com/api/v1.1/public/getmarkethistory?market=USDT-BTC')
    content=re.content
    trades=json.loads(content)
    date=[]
    price=[]
    amount=[]
    for trade in trades['result']:
        date.append(str(time.mktime(dateutil.parser.parse(trade['TimeStamp']).timetuple())))
        price.append(trade['Price'])
        amount.append(trade['Total'])
    return date,price,amount

def main():
    date,price,amount =get_trades()
    print(len(price))
    plt.figure()
    plt.plot(date, price)
    plt.show()

if __name__ == '__main__':
  main()



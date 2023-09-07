from bs4 import BeautifulSoup as bs
import pandas as pd
import pymysql
import time

import requests
try:

    connection = pymysql.connect(host='localhost',
                                        user='root',
                                        password='',
                                        database='magazinus',
                                        cursorclass=pymysql.cursors.DictCursor)
except:
    print("Нет коннекта к БД")
    exit()


URL_TEMPLATE = "https://store.artlebedev.ru/accessories/"
r = requests.get(URL_TEMPLATE)
print(r.status_code)

soup = bs(r.text, "html.parser")

price = soup.find_all('span', 'price_current_RUB')
for link in range(len(price)):
    fname = soup.find_all('span', 'product__name')[link].text
    #idd = soup.find_all('span' , "js-add-to-wishlist")[link].get('data-product-id')
    price = soup.find_all('span', class_ = 'price_current_RUB')[link].text
    #print(fname)
    #print(price)
    #print(idd)
    sql = "INSERT INTO magazinus (id,name,price) VALUES ('',%s,%s)"
    cursor=connection.cursor()
    cursor.execute(sql, (fname,price))
    connection.commit()
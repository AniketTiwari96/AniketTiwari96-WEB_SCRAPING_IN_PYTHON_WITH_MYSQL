from bs4 import BeautifulSoup
import requests , os
import pprint

import mysql.connector

def sending_data(val):
    mydb = mysql.connector.connect(host='localhost',
                                            database='carsData',
                                            user='root',
                                            password='Aniket@123')

    mycursor = mydb.cursor()

    sql = "INSERT INTO Data (car_name,car_price,year_,car_rating,car_model) VALUES (%s, %s, %s, %s, %s)"

    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
  

url='https://www.cars.com/shopping/results/?stock_type=all&makes%5B%5D=mercedes_benz&models%5B%5D=&list_price_max=&maximum_distance=20&zip='

def scrapper(url):
    response = requests.get(url)
    htmlcontent = response.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    lis = []
    res=soup.find_all('div',attrs={'class':'vehicle-card'})

    for i in res:
        car_name = i.find('h2',class_="title").get_text()[4:-1:1]
        year_ = i.find('h2',class_="title").get_text()[0:5:1]
        list_ = car_name.split(' ')
        car_model=list_[-2] +' '+list_[-1]
        car_price = i.find('div',class_="price-section price-section-vehicle-card").span.get_text()
        car_rating = i.find('div',class_="vehicle-dealer")
        try:
            car_rating = car_rating.find('span',class_="sds-rating__count").get_text()
        except(AttributeError):
            car_rating = None
        lis.append((car_name,car_price,year_,car_rating,car_model))
    if len(lis):
        sending_data(lis)
    else:
        print('invallide URL')
scrapper(url)
        
        
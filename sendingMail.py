import smtplib
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                                         database='carsData',
                                         user='root',
                                         password='Aniket@123')
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Data")

myresult = mycursor.fetchall()
server = smtplib.SMTP('smtp.gmail.com', 465)  
server.ehlo()
server.starttls()
server.login('dami66111@gmail.com','Demo@123')
server.sendmail('dami66111@gmail.com','anikettiwari274302@gmail.com',f'this is you data in the database :{myresult}')  
server.quit()

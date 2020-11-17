import mysql.connector

#creating local db instance
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")

#creating an object
mycursor=mydb.cursor()
#mycursor.execute("create database aayushdb")
mycursor.execute("show databases")
for db in mycursor:
    print(db)
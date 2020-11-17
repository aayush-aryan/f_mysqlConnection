import mysql.connector

mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="root",database="aayushdb")
mycursor=mydatabase.cursor()

#mycursor.execute("create table employee(empid int,name varchar(200), sal int(20))")
mycursor.execute("show tables")
for tble in mycursor:
    print(tble)
import mysql.connector

mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="root",database="aayushdb")
mycursor=mydatabase.cursor()

sqlQuerry= "INSERT INTO employee(empid,name,sal) VALUES(%s,%s,%s)"
#creating a touple
employees=[(11, "Aayush", 20000),(12,"Aryan",30000),(13,"Ankit",40000)]

mycursor.executemany(sqlQuerry,employees)
mydatabase.commit()

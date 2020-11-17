import mysql.connector

mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="root",database="aayushdb")
mycursor=mydatabase.cursor()

#mycursor.execute("select name from employee")
#myresult=mycursor.fetchone()

mycursor.execute("select * from employee")

myresult=mycursor.fetchall()

for row in myresult:
    print(row)

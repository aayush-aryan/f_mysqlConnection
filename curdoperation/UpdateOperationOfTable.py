import mysql.connector

mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="root",database="aayushdb")
mycursor=mydatabase.cursor()

sqlQuerry="UPDATE employee SET sal=90000 WHERE empid=12"
mycursor.execute(sqlQuerry)
mydatabase.commit()

mycursor.execute("select * from employee")

myresult=mycursor.fetchall()

for row in myresult:
    print(row)
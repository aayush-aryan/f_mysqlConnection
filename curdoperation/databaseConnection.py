import mysql.connector
mydB=mysql.connector.connect(host="localhost",user="root",passwd="root")
print(mydB)
if(mydB):
    print("connection is Successful")
else:
    print("connection is UnSuccessful")
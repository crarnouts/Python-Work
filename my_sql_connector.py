# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:22:02 2019

@author: arnou
"""

import mysql.connector

mydb = mysql.connector.connect(
        host = '127.0.0.1',
        #host = "localhost",
        user = "root",
        passwd = "Glhs171!",
        auth_plugin='mysql_native_password'
        #,
        #database = "testdb"
        
        )

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE testdb")



mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)







#mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")


#mycursor.execute("SHOW TABLES")

#for tb in mycursor:
#    print(tb)
    
sqlFormula = "INSERT INTO students (name,age) VALUES (%s,%s)"
students = [("Rachel",22),("Bob",22),("Chad",22),("Corey",25),("Rachel",31),]

mycursor.executemany(sqlFormula, students)

mydb.commit()
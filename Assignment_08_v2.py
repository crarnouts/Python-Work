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
        auth_plugin='mysql_native_password',
        database = "data602"
        
        )

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE testdb")



mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)


mycursor.execute("USE DATABASE testdb")


mycursor.execute("DROP DATABASE IF EXISTS data602")



mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")


mycursor.execute("SHOW TABLES")

for tb in mycursor:
   print(tb)
    
sqlFormula = "INSERT INTO students (name,age) VALUES (%s,%s)"
students = [("Rachel",22),("Bob",22),("Chad",22),("Corey",25),("Rachel",31),]

mycursor.executemany(sqlFormula, students)

mydb.commit()


mycursor.execute("SELECT age FROM students")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)


sql = "SELECT * FROM students WHERE age = 25"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)












import mysql.connector as mc
import pandas as pd
import unittest
from sklearn import datasets as ds





# Change password
def get_credentials():
    return {'user':'root','password':'Glhs171!'}


creds = get_credentials()


class Iris:
    def __init__(self,creds,dbname='data602',new=True):
        self.__conn = self.__get_connection(creds)
        self.__dbname = "Iris"

    # Drop the database and create a new one with a new table
    #def __create(self):
    def create(self):
        # ------ Place code below here \/ \/ \/ ------
        
        self.conn.cursor.execute("CREATE DATABASE testdb")
            
        #mycursor.execute("SHOW DATABASES")

        #for db in mycursor:
            #print(db)
            
        #return mycursor

        # ------ Place code above here /\ /\ /\ ------

    # Establish a connection
    def __get_connection(self,creds):
        return mc.connect(user=creds['user'], password=creds['password'],
                              host='127.0.0.1',
                              auth_plugin='mysql_native_password')      


        
    
    
    
    
    test = Iris(creds)
    
    test.create()
    
    mycursor = test.create()
    
    
    #mycursor = connection.cursor()

    #mycursor.execute("CREATE DATABASE testdb")



    mycursor.execute("SHOW DATABASES")
    
    for db in mycursor:
        print(db)

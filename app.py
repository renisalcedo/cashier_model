# this is the class that runs the database
from db.db import connectdb
from src.Employee import Employee

db = connectdb()

db_cursor = db.cursor()

# creating the database and the tables to make this module

db_cursor.execute("CREATE DATABASE IF NOT EXISTS STARBUCKS")
db_cursor.execute("USE STARBUCKS")

db_cursor.execute("CREATE TABLE IF NOT EXISTS DRINKS"
                  "(ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(255) NOT NULL, PRICE INT NOT NULL )")

db_cursor.execute("CREATE TABLE IF NOT EXISTS FOOD"
                  "(ID INT AUTO_INCREMENT PRIMARY KEY, TYPE VARCHAR (255) NOT NULL, NAME VARCHAR(255) NOT NULL,"
                  "PRICE INT NOT NULL )")

db_cursor.execute("CREATE TABLE IF NOT EXISTS MISC "
                  "(ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(255),PRICE INT NOT NULL )")

db_cursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INT AUTO_INCREMENT PRIMARY KEY,"
                  "FIRSTNAME VARCHAR(255), USERNAME VARCHAR (255), PASSWORD VARCHAR (255))")
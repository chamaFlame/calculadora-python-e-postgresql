import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
class postgreClass:
    #connection and cursor creation
    connection = psycopg2.connect(host='localhost', user='postgres', password='abcd')
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    #create database and tables if it doesn't exists already
    def __init__(self):
        if(self.checkIfDatabaseExists() == False):
            self.createDatabaseAndTable()
        else:
            self.connection = psycopg2.connect(database="calculator", host='localhost', user='postgres', password='abcd')
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor = self.connection.cursor()
    #check if the database already exists
    def checkIfDatabaseExists(self):
        self.cursor.execute("SELECT datname FROM pg_database")
        databases = self.cursor.fetchall()
        databasesArray=[]
        indexes = 0
        while indexes < len(databases):
            formattedName = str(databases[indexes])
            formattedName= formattedName.replace("(","").replace(")","").replace(",","").replace("\'","")
            indexes = indexes + 1
            databasesArray.append(formattedName)
        if "calculator" in databasesArray:
            return True
        else:
            return False
    #create the database and table
    def createDatabaseAndTable(self):
        self.cursor.execute("CREATE DATABASE calculator") 
        self.connection.commit()
        self.connection = psycopg2.connect(database="calculator", host='localhost', user='postgres', password='abcd')
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE savedCalcs(calcs FLOAT)")
        self.connection.commit()
    def dropDatabase(self):
        self.connection = psycopg2.connect(host='localhost', user='postgres', password='abcd')
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DROP DATABASE IF EXISTS calculator")
        self.connection.commit()
    def insertNewValue(self, newValue):
        command = "INSERT INTO savedCalcs VALUES(%s)"
        insertedValue = [float(newValue)]
        self.cursor.execute(command, insertedValue)
        self.connection.commit()
    def loadSaves(self):
        self.cursor.execute("SELECT * FROM savedCalcs")
        loads = self.cursor.fetchall()
        loadedValuesArray=[]
        indexes=0
        while indexes < len(loads):
            formattedName = str(loads[indexes])
            formattedName= formattedName.replace("(","").replace(")","").replace(",","")
            indexes = indexes + 1
            loadedValuesArray.append(float(formattedName))
        return loadedValuesArray
    def deleteAllSaves(self):
        self.cursor.execute("DELETE FROM savedCalcs")
        self.connection.commit()
    def deleteFirstRow(self):
        self.cursor.execute("DELETE FROM savedCalcs WHERE calcs IN (SELECT calcs FROM savedCalcs LIMIT 1)")
        self.connection.commit()
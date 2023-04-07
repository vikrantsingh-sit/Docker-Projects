#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cherrypy
import pandas as pd
import time
import mysql.connector
from datetime import datetime
import os
import cherrypy_cors


#usrname = os.environ['dbusr']
#password = os.environ['pass']

dataBase = mysql.connector.connect(
  host = 'mysql' ,
  user = "root" ,
  passwd = "secret"
)
 
print(dataBase)

Cursor = dataBase.cursor()
#Cursor.execute("CREATE DATABASE Calculator")
#print("Calculator Data base is created")

Cursor.execute( "CREATE TABLE Calculator.square (metric varchar(255))")

print("square table is created")

# Disconnecting from the server
dataBase.close()

class MyProcessor:     
    def run(self, df):        
        return (df*df)

p = MyProcessor()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def square(self):
        if cherrypy.request.method != 'POST':
            # This is a request that browser sends in CORS prior to
            # sending a real request.

            # Set up extra headers for a pre-flight OPTIONS request.
            
            cherrypy_cors.preflight(allowed_methods=['POST'])
            cherrypy.response.status = 200
            return("Allowed Method : POST")
        
        if cherrypy.request.method == 'POST':
            
            data = cherrypy.request.json
            df = pd.DataFrame(data)

            startTime = datetime.now()

            output = p.run(df)
            afterTime = datetime.now()

            difference = afterTime-startTime
            metric = difference.total_seconds()

            # Prepare the SQL query
            dataBase = mysql.connector.connect(
            host = 'mysql' ,
            user = "root"  ,
            passwd = "secret"
            ) 

            Cursor = dataBase.cursor()
            sql = "INSERT INTO Calculator.square (metric) VALUES (%s)"
            values = (metric,)

            # Execute the query
            Cursor.execute(sql, values)

            # Commit the changes
            dataBase.commit()

            # Print the number of rows affected
            print(Cursor.rowcount, "record inserted.")

            # Disconnecting from the server
            dataBase.close()
            return output.to_json()

if __name__ == '__main__':
   cherrypy_cors.install()
   config = {'server.socket_host': '0.0.0.0',
            'server.socket_port': 9090 ,
            'cors.expose.on': True}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())


# In[ ]:





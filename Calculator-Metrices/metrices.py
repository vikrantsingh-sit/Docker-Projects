#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import cherrypy
import mysql.connector
import json
import cherrypy_cors

#usrname = os.environ['dbusr']
#password = os.environ['pass']


class MyProcessor:     
    def run(self): 
        

        dataBase = mysql.connector.connect(
          host = 'mysql' ,
          user = "root"  ,
          passwd = "secret"
          ) 

        Cursor = dataBase.cursor()
        sql = "select * from Calculator.cube"
        # Execute the query
        Cursor.execute(sql)
        myresult = Cursor.fetchall()
        sum = 0
        for x in myresult:
            sum = float(x[0]) + sum
        cubrmet = sum/len(myresult)


        sql = "select * from Calculator.square"
        # Execute the query
        Cursor.execute(sql)
        myresult = Cursor.fetchall()
        sum = 0
        for x in myresult:
            sum = float(x[0]) + sum
        sqrmet = sum/len(myresult)


        sql = "select * from Calculator.fibonacci"
        # Execute the query
        Cursor.execute(sql)
        myresult = Cursor.fetchall()
        sum = 0
        for x in myresult:
            sum = float(x[0]) + sum
        fibmet = sum/len(myresult)


        #result = "square  : "+str(sqrmet)+"\n"+"Cube  : "+str(cubrmet)+"\n"+"Fibonacci  : "+str(fibmet)

        result = {'square': sqrmet, 'Cube' : cubrmet, 'Fibonacci' : fibmet}

        j = json.dumps(result)

        return(json.loads(j))


p = MyProcessor()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def metrices(self):
        if cherrypy.request.method != 'GET':
            # This is a request that browser sends in CORS prior to
            # sending a real request.

            # Set up extra headers for a pre-flight OPTIONS request.
            
            cherrypy_cors.preflight(allowed_methods=['GET'])
            cherrypy.response.status = 200
            return("Allowed Method : GET")

        if cherrypy.request.method == 'GET':
              output = p.run()
              return output

if __name__ == '__main__':
   cherrypy_cors.install()
   config = {'server.socket_host': '0.0.0.0',
            'server.socket_port': 2020 ,
            'cors.expose.on': True}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())


# In[ ]:





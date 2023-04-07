FROM python:3

WORKDIR /usr/src/app


RUN pip install mysql-connector-python
RUN pip install pandas
RUN pip install CherryPy
RUN pip install cherrypy-cors
COPY cube.py ./

EXPOSE 5050

ENTRYPOINT ["python", "cube.py"]
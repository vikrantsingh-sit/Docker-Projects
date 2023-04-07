FROM python:3

WORKDIR /usr/src/app


RUN pip install mysql-connector-python
RUN pip install CherryPy
RUN pip install cherrypy-cors
COPY metrices.py ./

EXPOSE 2020

ENTRYPOINT ["python", "metrices.py"]
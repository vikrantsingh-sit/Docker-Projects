FROM python:3

WORKDIR /usr/src/app


RUN pip install mysql-connector-python
RUN pip install pandas
RUN pip install CherryPy
RUN pip install cherrypy-cors
COPY fibonacci.py ./

EXPOSE 4040

ENTRYPOINT ["python", "fibonacci.py"]
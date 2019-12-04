FROM python:3
ADD main.py /
RUN pip install flask
RUN pip install flask_restful
RUN pip install sqlalchemy
RUN pip install redis
RUN pip install simplejson
CMD [ "python", "./main.py" ]


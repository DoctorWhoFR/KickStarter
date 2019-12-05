from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import sqlalchemy as db
import simplejson as json
import redis
import json
import jwt
import datetime
from time import perf_counter 

app = Flask(__name__)
api = Api(app)

redis_host = '172.19.0.2'

engine = db.create_engine('mysql+pymysql://root@localhost/kickstarter') #Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

projets_query = db.Table('projets', metadata, autoload=True, autoload_with=engine) # projects tables
users_tables = db.Table('users', metadata, autoload=True, autoload_with=engine) # projects tables

secret = "maYVPXbAvNOM4fNBeoqq_sE-x6eW_iw4ycl4vEJVd_4"

# GETTING ALL PROJECTS PER 20 PAGES
class AuthUser(Resource):
    def post(self):

        
        user_username = request.form['username']
        user_password = request.form['password']

        print(request.headers.get("Authorization"))
        t1_start = perf_counter() 

        try:        
            query = db.select([users_tables]).where(db.and_(users_tables.columns.username == user_username, users_tables.columns.password == user_password)) # the query 
            ResultProxy = connection.execute(query) # query execute 
            ResultSet = ResultProxy.fetchall() # fetchs alls rows of tables | ResultSet[] = ResultProxy(1, 'zefzef', 'zefezfezfzef', '') 
            time = datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
            encoded = jwt.encode({ 'exp': time, 'user':dict(ResultSet[0]) }, secret, algorithm='HS256')

            response_time = perf_counter() - t1_start

            return jsonify({'status': 'finished', 'response_time': response_time,  'result': encoded}) # transform into json response
        
        except (IndexError):
            response_time = perf_counter() - t1_start            

            return jsonify({'status': 'error', 'response_time': response_time,  'result': 'error_invalid_login'})     

api.add_resource(AuthUser, '/auth')  # POST ROUTE


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5001")

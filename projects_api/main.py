from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import sqlalchemy as db
import simplejson as json
import redis
import json
import jwt
from time import perf_counter 

app = Flask(__name__)
api = Api(app)

redis_host = '172.19.0.2'

engine = db.create_engine('mysql+pymysql://root@localhost/kickstarter') #Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

projets_query = db.Table('projets', metadata, autoload=True, autoload_with=engine) # projects tables

secret = "maYVPXbAvNOM4fNBeoqq_sE-x6eW_iw4ycl4vEJVd_4"

# GETTING ALL PROJECTS PER 20 PAGES
class GetProjetsPages(Resource):
    def get(self, page):
        t1_start = perf_counter() 

        try:
            jwt.decode(request.headers.get("Authorization"), secret, algorithms=['HS256'])
            
            query = db.select([projets_query]) # the query 
            
            ResultProxy = connection.execute(query) # query execute 
            ResultSet = ResultProxy.fetchall() # fetchs alls rows of tables | ResultSet[] = ResultProxy(1, 'zefzef', 'zefezfezfzef', '') 

            json_data=[]
            start = int(page) * 20

            for result in ResultSet[:start]:
                json_data.append(dict(result)) # transform ResultProxy into an array of object response 

            response_time = perf_counter() - t1_start

            return jsonify({'status': 'finished', 'response_time': response_time, 'result_page': int(page),  'result': json_data}) # transform into json response
        except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
            return "ExpiredSignatureError"

        

# GETTING ALL PROJECTS
class GetProjets(Resource):
    def get(self):

        t1_start = perf_counter() 

        try:
            jwt.decode(request.headers.get("Authorization"), secret, algorithms=['HS256'])
            query = db.select([projets_query]) # the query 
            ResultProxy = connection.execute(query) # query execute 
            ResultSet = ResultProxy.fetchall() # fetchs alls rows of tables | ResultSet[] = ResultProxy(1, 'zefzef', 'zefezfezfzef', '') 

            json_data=[]

            for result in ResultSet:
                json_data.append(dict(result)) # transform ResultProxy into an array of object response 

            response_time = perf_counter() - t1_start

            return jsonify({'status': 'finished',  'response_time': response_time, 'result_count': len(json_data),  'result': json_data}) # transform into json response
        except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
            return "ExpiredSignatureError"


class PostProjet(Resource):
    def post(self):
        t1_start = perf_counter() 
        
        try:
            jwt.decode(request.headers.get("Authorization"), secret, algorithms=['HS256'])

            projets_title = request.form['title']
            projets_description = request.form['description']
            projets_author = request.form['author']
            
            wanted_price = request.form['wanted_price']

            query = db.insert(projets_query).values(name=projets_title, description=projets_description, author=projets_author, wanted_price=wanted_price) 
            
            ResultProxy = connection.execute(query)

            response_time = perf_counter() - t1_start

            return {'status': 'added', 'response_time': response_time}
        except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
            return "ExpiredSignatureError"

class GetProjet(Resource):
    def get(self, id):

        try:
            jwt.decode(request.headers.get("Authorization"), secret, algorithms=['HS256'])

            query = db.select([projets_query]).where(projets_query.columns.id == id)
            ResultProxy = connection.execute(query)
            ResultSet = ResultProxy.fetchall()

            return jsonify({'status': 'finished',  'result': dict(ResultSet[0])})

        except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
            return "ExpiredSignatureError"

api.add_resource(GetProjetsPages, '/projets/<page>')  # GET ALLS PROJETS PER 20 ROUTES
api.add_resource(GetProjets, '/projets/') # GET ALLS PROJETS
api.add_resource(GetProjet, '/projet/<id>') # GET PROJET ROUTES
api.add_resource(PostProjet, '/projets')  # POST ROUTE


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0')

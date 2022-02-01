from flask import Flask
from flask_restful import Api, Resource
from pymongo import MongoClient
from passbox import password

app = Flask(__name__)
api = Api(app)

class Todos(Resource):

    def connect_to_mongo(self, database):
        client = MongoClient(f"mongodb+srv://SDido:{password}@cluster0.xtvv1.mongodb.net/{database}?retryWrites=true&w=majority")
        db = client.get_database(database)
        records = db.todos
        return records

    def get(self):
        records = self.connect_to_mongo('Family')
        all_records = list(records.find())
        return {"data": all_records}

    # def post(self):

api.add_resource(Todos, "/family-todos")


if __name__ == "__main__":
    app.run(debug=True)
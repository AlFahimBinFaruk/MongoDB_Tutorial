from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb+srv://mongo:mongo@cluster0.pcwyrxd.mongodb.net/blog?retryWrites=true&w=majority"
mongo = PyMongo(app)

if __name__ == "__main__":
    # get data
    @app.get("/")
    def handleGet():
        allData = mongo.db.test.find().limit(6)
        data = json.loads(json_util.dumps(allData))
        return data
    
    # add new data
    @app.post("/add")
    def handleAdd():
        name = request.json.get("name")
        role = request.json.get("role")

        newData = {"name":name,"role":role}
        mongo.db.test.insert_one(newData)
        return jsonify({"msg":"data added"})    

    # start server.    
    app.run(debug=True)
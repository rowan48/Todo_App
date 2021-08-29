from flask import Flask, render_template,request,redirect,url_for
import json
import simplejson as json
#from flask.wrappers import JSONMixin
#from flask.wrappers import JSONMixin # For flask implementation    
from bson import ObjectId # For ObjectId to work  
from bson.json_util import dumps, loads
from pymongo import MongoClient    
import os 
from time import time  
import redis


    
app = Flask(__name__) 

#cache = redis.Redis(host='127.0.0.1', port=6379)
#def get_hit_count():
#    retries = 5
#    while True:
#        try:
#            return cache.incr('hits')
#        except redis.exceptions.ConnectionError as exc:
#            if retries == 0:
#                raise exc
#            retries -= 1
#            time.sleep(0.5)
title = "TODO"    
heading = "TODO-APP"    
    
client = MongoClient("mongodb://127.0.0.1:27017") #host uri    
db = client.mymongodb    #Select the database    
todos = db.todo #Select the collection name 
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017"
#cursor = todos.find()
#list_cur = list(cursor)
#json_data = dumps(list_cur, indent = 2) 
# Writing data to file data.json
#with open('data.json', 'w') as file:
    #file.write(json_data)


   
    
def redirect_url():
	return request.args.get('next') or \
		request.referrer or \
		url_for('index')
  
@app.route("/list")    #mylist
def lists ():    
    #Display the all Tasks    
    todos_l = todos.find()   
    a1="active" 
    list_cur = list(todos_l)
    json_data = dumps(list_cur, indent = 2) 
    return(json_data)


    #return render_template('index.html',a1=a1,todos=todos_l,t=title,h=heading)    
@app.route('/list', methods=["POST"])
def post():
    #body of the post request 
    new_todo = {'addtodo' : request.json['addtodo']} 
    todos.insert_one(new_todo)    
    return 'done'
  
@app.route('/')    
@app.route("/action", methods=['POST'])    
def action ():    
    #Adding a Task    
    name=request.values.get("name")    
    desc=request.values.get("desc")    
    #date=request.values.get("date")    
    #pr=request.values.get("pr")    
    todos.insert({ "name":name, "desc":desc, "done":"no"}) 
    #todos.insert({ "name":name, "desc":desc, "date":date, "pr":pr, "done":"no"}) 
    #todos.insert({ "name":name, "done":"no"}) 
    return redirect("/list") 
    #return(True)   
  
@app.route("/delete", methods=["DELETE"])   #delete 
def remove ():    
    #Deleting a Task with various references    
    key=request.values.get("_id")    
    todos.remove({"_id":ObjectId(key)})    
    #return redirect("/")
    #return(True)   
    return'deleted'
@app.route("/update", methods=["PUT"])  #update  
def update ():    
    id=request.values.get("_id")    
    task=todos.find({"_id":ObjectId(id)})    
    #return render_template('update.html',tasks=task,h=heading,t=title) 
    #return redirect("/") 
    return'updated'
  
@app.route("/action3", methods=['POST'])    
def action3 ():    
    #Updating a Task with various references    
    name=request.values.get("name")    
    desc=request.values.get("desc")    
    #date=request.values.get("date")    
    #pr=request.values.get("pr")    
    id=request.values.get("_id")    
    #todos.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "desc":desc, "date":date, "pr":pr }})    
    todos.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "desc":desc}})    
    return redirect("/") 
    #return(True)   

#@app.route("/search", methods=['GET'])    
#def search():    
    #Searching a Task with various references    
    
 #   key=request.values.get("key")    
  #  refer=request.values.get("refer")    
   # if(key=="_id"):    
    #    todos_l = todos.find({refer:ObjectId(key)})    
    #else:    
     #   todos_l = todos.find({refer:key})    
    #return render_template('searchlist.html',todos=todos_l,t=title,h=heading)    
    
if __name__ == "__main__":    
    
    app.run()   
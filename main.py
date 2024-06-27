from flask import Flask, request

app = Flask('__name__')
@app.route("/")
def index() :
  with open('index.html', 'r') as file : 
    data = file.read()
  return data
@app.route("/page") 
def page() : 
  return 'hello'
app.runt(host="0.0.0.0", port=8080)

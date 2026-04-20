from flask import Flask, request

app = Flask(__name__)
tasks = []

@app.route('/')
def home():
    return "<h1>To-Do</h1>" + str(tasks) + \
           "<form action='/add' method='post'>" \
           "<input name='task'><button>Add</button></form>"

@app.route('/add', methods=['POST'])
def add():
    tasks.append(request.form['task'])
    return "Added <a href='/'>Back</a>"

app.run()
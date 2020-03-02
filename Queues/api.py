from flask import Flask, request, jsonify
from workers_queue import WorkersQueue

workers = None

app = Flask(__name__)

@app.route('/push', methods= ['GET'])
def push():
    data = request.args
    if (workers == None):
        workers = WorkersQueue(data)
    else:
        workers.push(data)

@app.route('/pop', methods= ['GET'])
def pop():
    data = request.args
    if (workers != None):
        workers.pop()




if __name__ == "__main__":
    app.run(debug=True, port=8080)
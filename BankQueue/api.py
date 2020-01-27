from flask import Flask, request,jsonify
import bank_queue

q = bank_queue.BankQueue()

app = Flask(__name__)

@app.route('/push', methods= ['POST'])
def push():
	return jsonify({'Queue': q.push(request.args.get('operation'))})

@app.route('/clear', methods= ['GET'])
def clear():
	return jsonify({'Queue': q.clear() })

@app.route('/pop', methods= ['GET'])
def pop():
	return jsonify({'Queue': q.pop() })

@app.route('/view_queue', methods= ['GET'])
def view_queue():
	return jsonify({'Queue': q.queue })

if __name__ == "__main__":
    app.run(debug=True,port=8080)
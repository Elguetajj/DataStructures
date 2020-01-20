from flask import Flask, request,jsonify

app = Flask(__name__)

def sum_naturals(n):
    return int(n) * (int(n) + 1) / 2 if int(n) >= 1 else "n is not natural"


@app.route('/naturals', methods= ['POST'])
def home():
    return jsonify({"sum" : sum_naturals(request.args.get('n'))})

if __name__ == "__main__":
    app.run(debug=True,port=8080)
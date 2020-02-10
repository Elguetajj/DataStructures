from flask import Flask, request,jsonify
import topchars

app = Flask(__name__)

@app.route('/topchars', methods= ['GET'])
def get_topchars():
    text = request.json
    return jsonify({'top_chars': topchars.topchars.countchars(text['text'])})

if __name__ == "__main__":
    app.run(debug=True,port=8080)
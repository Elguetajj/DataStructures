from flask import Flask, request,jsonify
import point

app = Flask(__name__)

@app.route('/quadrant', methods= ['GET'])
def get_topchars():
    pnt = point.POINT(int(request.args.get("x")),int(request.args.get("y")))
    return jsonify({'Quadrant': point.quadrant(pnt)})

if __name__ == "__main__":
    app.run(debug=True,port=8080)
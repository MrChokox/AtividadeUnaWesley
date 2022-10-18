import math
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calcularDistancia/<float:x1>/<float:x2>/<float:y1>/<float:y2>', methods=['GET'])
def getDistancia(x1,x2,y1,y2):
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    distancia = math.sqrt(x + y)
    return jsonify({'distancia': distancia});

if __name__ == '__main__':
  app.run(debug = True, port = 5000)
# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/produtos
@app.route('/salario', methods=['GET'])
def retornar_todos_os_produtos():
    horas = int(request.headers['horas'])*40
    extras = int(request.headers['extras'])*50

    bruto = round(horas+extras, 2)
    liquido = round(bruto-(bruto * 0.1), 2)

    
    salarios = [{'bruto': 'R$' + str(bruto),
                'liquido': 'R$' + str(liquido)}]
    return jsonify(salarios)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)
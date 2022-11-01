# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    pequeno = round(int(request.headers['pequeno'])*10, 2)
    medio = round(int(request.headers['medio'])*12, 2)
    grande = round(int(request.headers['grande'])*15, 2) 
    total = round(pequeno + medio + grande, 2)

    camisas = [{'pequeno': 'R$' + str(pequeno),
                'medio': 'R$' + str(medio),
                'grande': 'R$' + str(grande),
                'total': 'R$' + str(total)}]
    return jsonify(camisas)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)
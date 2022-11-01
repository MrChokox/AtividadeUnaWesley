# Importar a classe Flask e o objeto request:
from flask import Flask, request
# Criar o objeto Flask app:
app = Flask(__name__)

@app.route('/teste/1', methods=['POST'])
def teste_json():
    objeto_json = request.get_json()    
    print(objeto_json)
    x = objeto_json['X']
    y = objeto_json['Y']
    z = objeto_json['Z']

    if (x + y <= z) or (x + z <= y) or (y + z <= x) :
        return 'Não é um Triangulo!'  
    else:
        return 'É um Triangulo!'


@app.route('/teste/2', methods=['POST'])
def teste_json2():
    objeto_json = request.get_json()    
    print(objeto_json)
    x = objeto_json['X']

    match x:
        case 1:
            return 'Produto:Sapato ||Preço:R$ 99,99'
        case 2:
            return 'Produto:Bolsa ||Preço:R$ 103,89'
        case 3:
            return 'Produto:Camisa ||Preço:R$ 49,98'
        case 4:
            return 'Produto:Calça ||Preço:R$ 89,72'
        case 5:
            return 'Produto:Blusa ||Preço:R$ 97,35'
        case _:
            return 'Não tem Produto cadastrado com esse codigo'



if __name__ == '__main__':
    app.run(debug = True, port = 5000)
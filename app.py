from flask import Flask, jsonify, request
app = Flask(__name__)

livros = [
  { 
   'id': 1,
   'titulo': 'senhor dos aneis',
   "autor": 'J,R,R Toçkien' 
  },
  { 
   'id': 2,
   'titulo': 'Harry poter',
   "autor": 'J.K Howling' 
  },  
  { 
   'id': 3,
   'titulo': 'Habitos atomicos',
   "autor": 'James Clear' 
  },
]


#consultar todos
@app.route('/livros', methods=["GET"])
def obterLivros():
  return jsonify(livros)
#consultar por id
@app.route('/livros/<int:id>', methods=["GET"])
def obterLivroPorId(id):
  for livro in livros:
    if livro.get('id') == id:
      return jsonify(livro)

@app.route('/livros/<int:id>', methods=["PUT"])
def editarLivroPorId(id):
  livroAlterado = request.get_json()#pega o json da req do user

  for indice,livro in enumerate(livros):
    # print('indice ', indice, " livro ", livro)
    if livro.get('id') == id:
      livros[indice].update(livroAlterado)
      return jsonify(livros[indice])

@app.route("/livros",methods=["POST"])
def incluirNovoLivro():
  novoLivro = request.get_json()
  livros.append(novoLivro)
  return jsonify(livros)


@app.route('/livros/<int:id>',methods=["DELETE"])
def excluirLivro(id):
  for indice,livro in enumerate(livros):
    if livro.get('id') == id:
      del livros[indice]
  return jsonify(livros)
app.run(port=5000,host='localhost',debug=True)
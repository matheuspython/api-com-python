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
@app.route('/livros')
def obterLivros():
  return jsonify(livros)


app.run(port=5000,host='localhost',debug=True)
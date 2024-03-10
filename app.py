from flask import Flask, jsonfy, request 
app = Flask(__name__)

livos = [
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
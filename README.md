# API de Gerenciamento de Livros

Esta é uma API simples criada em Flask para gerenciamento de livros.

## Funcionalidades

- Consultar todos os livros.
- Consultar um livro por ID.
- Editar um livro por ID.
- Incluir um novo livro.
- Excluir um livro por ID.

## Endpoints

### Consultar todos os livros

`GET /livros`

Retorna todos os livros cadastrados.

### Consultar um livro por ID

`GET /livros/<int:id>`

Retorna um livro específico com o ID correspondente.

### Editar um livro por ID

`PUT /livros/<int:id>`

Edita um livro existente com o ID correspondente.

### Incluir um novo livro

`POST /livros`

Inclui um novo livro na lista de livros.

### Excluir um livro por ID

`DELETE /livros/<int:id>`

Exclui um livro existente com o ID correspondente.

## Uso

1. Clone o repositório:

git clone https://github.com/seu_nome/nome_do_repositorio.git

2. Instale as dependências:

pip install flask


3. Execute a aplicação:

python app.py


Certifique-se de substituir `http://localhost:5000` pelo host e porta onde o servidor Flask está sendo executado.

## Observações

- Esta é uma aplicação de exemplo e não deve ser usada em produção sem implementações de segurança adequadas.
- Consulte a documentação do Flask para mais informações sobre como expandir e configurar a aplicação.



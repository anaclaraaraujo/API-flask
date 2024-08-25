# E-Commerce API

Esta é uma API de e-commerce desenvolvida com Flask, que inclui funcionalidades para autenticação de usuários, gerenciamento de produtos e carrinho de compras.

## Funcionalidades

- **Autenticação de Usuário**: Login e Logout
- **Gerenciamento de Produtos**: Adicionar, Atualizar, Deletar e Visualizar produtos
- **Carrinho de Compras**: Adicionar, Remover e Visualizar itens no carrinho, além de realizar o checkout

## Tecnologias Utilizadas

- **Flask**: Framework web para Python
- **Flask-SQLAlchemy**: ORM para interagir com o banco de dados SQLite
- **Flask-CORS**: Permite solicitações Cross-Origin
- **Flask-Login**: Gerenciamento de sessões e autenticação de usuários
- **SQLite**: Banco de dados

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/anaclaraaraujo/ecommerce-rest-api.git
   cd seurepositorio
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicialize o banco de dados (execute o shell Python):

   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   ```

5. Execute a aplicação:

   ```bash
   python app.py
   ```

   A aplicação estará disponível em `http://127.0.0.1:5000`.

## Endpoints

### Autenticação

- **POST /login**: Realiza login de um usuário.
  - Body: `{ "username": "usuario", "password": "senha" }`
  - Sucesso: `{"message": "Logged in successfully"}`
  - Falha: `{"message": "Unauthorized. Invalid credentials"}`

- **POST /logout**: Realiza logout do usuário atual.
  - Sucesso: `{"message": "Logout successfully"}`

### Produtos

- **POST /api/products/add**: Adiciona um novo produto.
  - Body: `{ "name": "Nome do Produto", "price": 10.0, "description": "Descrição do Produto" }`
  - Sucesso: `{"message": "Product added successfully"}`
  - Falha: `{"message": "Invalid product data"}`

- **DELETE /api/products/delete/<int:product_id>**: Deleta um produto.
  - Sucesso: `{"message": "Product deleted successfully"}`
  - Falha: `{"message": "Product not found"}`

- **GET /api/products/<int:product_id>**: Obtém detalhes de um produto.
  - Sucesso: `{"id": 1, "name": "Nome do Produto", "price": 10.0, "description": "Descrição do Produto"}`
  - Falha: `{"message": "Product not found"}`

- **PUT /api/products/update/<int:product_id>**: Atualiza um produto.
  - Body: `{ "name": "Novo Nome", "price": 20.0, "description": "Nova Descrição" }`
  - Sucesso: `{"message": "Product updated successfully"}`
  - Falha: `{"message": "Product not found"}`

- **GET /api/products**: Obtém a lista de todos os produtos.
  - Sucesso: `[ { "id": 1, "name": "Nome do Produto", "price": 10.0, "category": "category_generic" } ]`

### Carrinho de Compras

- **POST /api/cart/add/<int:product_id>**: Adiciona um produto ao carrinho.
  - Sucesso: `{"message": "Item added to the cart successfully"}`
  - Falha: `{"message": "Failed to add item to the cart"}`

- **DELETE /api/cart/remove/<int:product_id>**: Remove um produto do carrinho.
  - Sucesso: `{"message": "Item removed from the cart successfully"}`
  - Falha: `{"message": "Failed to remove item from the cart"}`

- **GET /api/cart**: Visualiza os itens no carrinho.
  - Sucesso: `[ { "id": 1, "user_id": 1, "product_id": 1, "product_name": "Nome do Produto", "product_price": 10.0 } ]`

- **POST /api/cart/checkout**: Realiza o checkout e limpa o carrinho.
  - Sucesso: `{"message": "Checkout successful. Cart has been cleared."}`

## Contribuindo

Sinta-se à vontade para contribuir com o projeto! Faça um fork, crie uma branch, e envie um pull request com suas melhorias.

```
Sinta-se à vontade para ajustar conforme necessário! 
Se precisar de mais alguma coisa, é só falar. 🤎
```
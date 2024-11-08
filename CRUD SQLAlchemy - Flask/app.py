from models import db, Produtos
from flask import Flask, request, render_template, redirect, abort
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_table():
    db.create_all()

@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
    
    if request.method == 'POST':
        produto_id = request.form['produto_id']
        name = request.form['name']
        tamanho = request.form['tamanho']
        preco = request.form['preco']
        produto = Produtos(produto_id=produto_id, name=name, tamanho=tamanho, preco=preco)
        db.session.add(produto)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def RetrieveList():
    produtos = Produtos.query.all()
    return render_template('datalist.html', produtos=produtos)

@app.route('/data/<int:id>')
def RetrieveEmployee(id):
    produto = Produtos.query.filter_by(id=id).first()
    if produto:
        return render_template('data.html', produto=produto)
    return f"Produto with id = {id} doesn't exist"

@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    produto = Produtos.query.filter_by(id=id).first()
    if request.method == 'POST':
        if produto:
            produto.name = request.form['name']
            produto.tamanho = request.form['tamanho']
            produto.preco = request.form['preco']
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Produto com id = {id} não encontrado", 404
    
    return render_template('update.html', produto=produto)


@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    produto = Produtos.query.filter_by(id=id).first()
    if request.method == 'POST':
        if produto:
            db.session.delete(produto)
            db.session.commit()
            return redirect('/data')
        else:
            return f"Produto with id = {id} not found", 404  # Mais descritivo

    return render_template('delete.html', produto=produto)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produtos(db.Model):
    __tablename__ = "produtos"  # Renomeei a tabela para 'employees' (não é obrigatório, mas mais claro)
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String())
    tamanho = db.Column(db.String(3))
    preco = db.Column(db.Float(80))

    def __init__(self, produto_id, name, tamanho, preco):
        self.produto_id = produto_id
        self.name = name
        self.tamanho = tamanho
        self.preco = preco

    def __repr__(self):
        return f"{self.name}: {self.produto_id}"

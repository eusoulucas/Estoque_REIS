import sqlite3

coneccao_user = sqlite3.connect('usuario_data.db')
coneccao_products = sqlite3.connect('produtos_data.db')

ponta = coneccao_user.cursor()

ponta.execute("""
	CREATE TABLE IF NOT EXISTS Usuarios (
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nome TEXT NOT NULL,
	Email TEXT NOT NULL,
	Usuario TEXT NOT NULL,
	Senha TEXT NOT NULL
	);
	""")

ponta1 = coneccao_products.cursor()

ponta1.execute('''
	CREATE TABLE IF NOT EXISTS Produtos(
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nome TEXT NOT NULL,
	Classe TEXT NOT NULL,
	Tamanho REAL NOT NULL,
	Preco REAL NOT NULL,
	Quantidade INTEGER NOT NULL,
	Marca TEXT NOT NULL
	)
	''')
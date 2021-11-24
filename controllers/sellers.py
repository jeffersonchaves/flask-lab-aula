from __main__ import app, connection
from flask import render_template

@app.route("/")
@app.route("/vendedores")
@app.route("/listar_vendedores")
def listar_vendedores():

    conn = connection.get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM seller")
    vendedores = c.fetchall()
    for row in vendedores:
        print(row)

    return 'vendedores'

@app.route("/vendedores/<id>")
def obter_por_id(id):
    return f'obter por id: {id}'

@app.route("/vendedores/cadastrar")
def cadastrar():
    return "mostrar formulario de cadastro"


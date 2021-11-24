from flask import Flask
from database.ConnectionFactory import ConnectionFactory

app = Flask(__name__)  # sao 2 underlines antes e 2 depois

connection = ConnectionFactory(app)

from controllers import sellers

# rodar nossa aplicacao
if __name__ == "__main__":
    app.run(debug=True)

from flaskext.mysql import MySQL, pymysql

class ConnectionFactory:
    app = None

    def __init__(self, app):
        self.app = app
        self.app.config['MYSQL_DATABASE_USER'] = 'root'
        self.app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
        self.app.config['MYSQL_DATABASE_DB'] = 'flask_vendedores'
        self.app.config['MYSQL_DATABASE_HOST'] = 'localhost'

        self.mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)
        self.mysql.init_app(self.app)


    def get_connection(self):
        self.mysqlConnection = self.mysql.connect()
        return self.mysqlConnection

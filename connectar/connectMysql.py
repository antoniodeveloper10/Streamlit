import mysql.connector
from mysql.connector import Error


class MySQLConnection:

    """
    Classe responsável por gerenciar conexão e transações no MySQL.
    """

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Estabelece a conexão e desativa o autocommit (modo transacional)."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                autocommit=False
            )
            self.cursor = self.connection.cursor()
            print("✅ Conexão MySQL estabelecida com sucesso.")
        except Error as e:
            print("❌ Erro ao conectar:", e)
            raise

    def execute(self, sql, params=None):
        """Executa um comando SQL único."""
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
        except Error as e:
            print("❌ Erro ao executar SQL:", e)
            raise

    def executemany(self, sql, data):
        """Executa vários inserts em lote."""
        try:
            self.cursor.executemany(sql, data)
        except Error as e:
            print("❌ Erro ao executar múltiplos inserts:", e)
            raise

    def commit(self):
        """Confirma a transação."""
        try:
            self.connection.commit()
            print("💾 Transação confirmada.")
        except Error as e:
            print("❌ Erro no commit:", e)
            raise

    def rollback(self):
        """Desfaz todas as operações não confirmadas."""
        try:
            self.connection.rollback()
            print("↩️ Rollback executado — transação desfeita.")
        except Error as e:
            print("❌ Erro no rollback:", e)
            raise

    def close(self):
        """Fecha cursor e conexão."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("🔒 Conexão MySQL encerrada.")

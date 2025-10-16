import oracledb

class OracleConnection:
    """
    Classe responsável por gerenciar a conexão com o banco de dados Oracle.
    """

    def __init__(self, user, password, dsn, encoding="UTF-8"):
        """
        Inicializa a conexão.
        :param user: Usuário do Oracle.
        :param password: Senha do Oracle.
        :param dsn: Data Source Name (ex: 'localhost:1521/xe' ou TNS configurado).
        :param encoding: Padrão de codificação.
        """
        self.user = user
        self.password = password
        self.dsn = dsn
        self.encoding = encoding
        self.connection = None
        self.cursor = None

    def connect(self):
        """Estabelece a conexão com o Oracle."""
        try:
            self.connection = oracledb.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn,
                encoding=self.encoding
            )
            self.cursor = self.connection.cursor()
            print("✅ Conexão Oracle estabelecida com sucesso.")
        except oracledb.DatabaseError as e:
            print("❌ Erro ao conectar ao Oracle:", e)
            raise

    def execute(self, query, params=None, commit=False):
        """
        Executa um comando SQL (INSERT, UPDATE, DELETE, SELECT, etc).
        :param query: Comando SQL.
        :param params: Parâmetros (tuple ou dict).
        :param commit: Se True, realiza commit automaticamente.
        :return: Resultado do SELECT (se houver).
        """
        try:
            if self.cursor is None:
                raise Exception("Conexão não inicializada. Use connect() primeiro.")

            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()

            if commit:
                self.connection.commit()

        except oracledb.DatabaseError as e:
            print("❌ Erro ao executar SQL:", e)
            self.connection.rollback()
            raise

    def executemany(self, query, data, commit=False):
        """
        Executa múltiplos inserts/updates em lote.
        :param query: SQL com bind variables.
        :param data: Lista de tuplas ou dicionários.
        :param commit: Se True, realiza commit.
        """
        try:
            self.cursor.executemany(query, data)
            if commit:
                self.connection.commit()
        except oracledb.DatabaseError as e:
            print("❌ Erro ao executar múltiplas operações:", e)
            self.connection.rollback()
            raise

    def commit(self):
        """Confirma as alterações."""
        if self.connection:
            self.connection.commit()

    def close(self):
        """Fecha a conexão e o cursor."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("🔒 Conexão Oracle encerrada.")

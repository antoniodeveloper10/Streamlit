import json
import os

from connectar.connectMysql import MySQLConnection  # Supondo que a classe esteja nesse arquivo

conn = MySQLConnection(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database=os.getenv("DB_NAME", "")
)




def update_tarefa(id_tarefa, dados_json):
    resultado = False
    try:
        print('chequei aqui para atualizar')
        dados = json.loads(dados_json)
        print(dados)
        conn.connect()
        print('conectei')
        print('tarefa ' + dados["Tarefa nº"])

        tarefa_num = id_tarefa
        data_batelada = dados["Data Batelada"]
        turno = dados["Turno"]
        moinho = dados["Moinho"]
        data_moagem = dados["Data Moagem"]
        silo = dados["Silo"]
        qtd_bateladas = dados["Quantidade Bateladas"]
        toneladas = dados["Toneladas"]
        hora_inicial = dados["Hora Inicial"]
        hora_final = dados["Hora Final"]
        data_envase = dados["Data Envase"]
        qtd_scs = dados["Qtd scs"]
        perda_scs = dados["Perda scs"]
        lote_completo = dados["Lote Completo"]
        produto = dados["Produto"]

        # 1️⃣ Atualizar BATELADA
        sql_batelada = """
        UPDATE BATELADA
        SET DATA_BATELADA = %s,
            TURNO = %s,
            MOINHO = %s,
            DATA_MOAGEM = %s,
            SILO = %s,
            QTD_BATELADAS = %s,
            TONELADAS = %s,
            HORA_INICIAL = %s,
            HORA_FINAL = %s,
            DATA_ENVASE = %s,
            QTD_SCS = %s,
            PERDA_SCS = %s,
            LOTE_COMPLETO = %s,
            PRODUTO = %s
        WHERE TAREFA_NUM = %s
        """

        conn.execute(sql_batelada, (
            data_batelada,
            turno,
            moinho,
            data_moagem,
            silo,
            qtd_bateladas,
            toneladas,
            hora_inicial,
            hora_final,
            data_envase,
            qtd_scs,
            perda_scs,
            lote_completo,
            produto,
            tarefa_num
        ))

        print('✅ Atualizei BATELADA')

        # 2️⃣ Atualizar OPERADOR_BATELADA
        # Estratégia: excluir antigos e inserir novos (para simplificar)
        conn.execute("DELETE FROM OPERADOR_BATELADA WHERE TAREFA_NUM = %s", (tarefa_num,))

        sql_operador = """
            INSERT INTO OPERADOR_BATELADA (TAREFA_NUM, TIPO_OPERACAO, NOME_OPERADOR)
            VALUES (%s, %s, %s)
        """

        if "Operador Bateladas" in dados:
            for nome in dados["Operador Bateladas"]:
                conn.execute(sql_operador, (tarefa_num, "BATELADA", nome))

        if "Operador Envase" in dados:
            for nome in dados["Operador Envase"]:
                conn.execute(sql_operador, (tarefa_num, "ENVASE", nome))

        print('✅ Atualizei OPERADOR_BATELADA')

        # 3️⃣ Atualizar AMOSTRAS
        conn.execute("DELETE FROM AMOSTRA_BATELADA WHERE TAREFA_NUM = %s", (tarefa_num,))
        sql_amostra = """
            INSERT INTO AMOSTRA_BATELADA (TAREFA_NUM, NUMERO_AMOSTRA)
            VALUES (%s, %s)
        """
        amostras = [(tarefa_num, str(i + 1)) for i in range(4)]
        conn.executemany(sql_amostra, amostras)
        print('✅ Atualizei AMOSTRA_BATELADA')

        # 4️⃣ Atualizar MATERIAS-PRIMAS
        conn.execute("DELETE FROM MATERIA_PRIMA_BATELADA WHERE TAREFA_NUM = %s", (tarefa_num,))
        materias_primas = dados["Materias primas"]

        sql_materia = """
            INSERT INTO MATERIA_PRIMA_BATELADA (TAREFA_NUM, NOME, QUANTIDADE, LOTE)
            VALUES (%s, %s, %s, %s)
        """

        valores = [
            (tarefa_num, nome, item["Quantidade"], item["Lote"])
            for nome, item in materias_primas.items()
        ]
        conn.executemany(sql_materia, valores)
        print('✅ Atualizei MATERIA_PRIMA_BATELADA')

        # Confirma tudo
        conn.commit()
        resultado = True

    except Exception as e:
        print("🚨 Erro detectado:", e)
        conn.rollback()
        return resultado

    finally:
        conn.close()
        return resultado


def save_tarefa(dados_json):
    resultado = False
    try:
        print('chequei aqui para salvar')
        dados = json.loads(dados_json)
        print(dados)
        conn.connect()
        print('conectei')
        print('tarefa ' + dados["Tarefa nº"])

        tarefa_num = dados["Tarefa nº"]
        data_batelada = dados["Data Batelada"]
        turno = dados["Turno"]
        moinho = dados["Moinho"]
        data_moagem = dados["Data Moagem"]
        silo = dados["Silo"]
        qtd_bateladas = dados["Quantidade Bateladas"]
        toneladas = dados["Toneladas"]
        hora_inicial = dados["Hora Inicial"]
        hora_final = dados["Hora Final"]
        data_envase = dados["Data Envase"]
        qtd_scs = dados["Qtd scs"]
        perda_scs = dados["Perda scs"]
        lote_completo = dados["Lote Completo"]
        produto = dados["Produto"]




        # 1️⃣ Inserir BATELADA
        sql_batelada = """
        INSERT INTO BATELADA (
            TAREFA_NUM, DATA_BATELADA, TURNO, MOINHO, DATA_MOAGEM, SILO,
            QTD_BATELADAS, TONELADAS, HORA_INICIAL, HORA_FINAL,
            DATA_ENVASE, QTD_SCS, PERDA_SCS, LOTE_COMPLETO, PRODUTO
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        """

        conn.execute(sql_batelada, (
            tarefa_num,
            data_batelada,
            turno,
            moinho,
            data_moagem,
            silo,
            qtd_bateladas,
            toneladas,
            hora_inicial,
            hora_final,
            data_envase,
            qtd_scs,
            perda_scs,
            lote_completo,
            produto
        ))

        print('inseriei bateladas')

        sql_operador = """
               INSERT INTO OPERADOR_BATELADA (TAREFA_NUM, TIPO_OPERACAO, NOME_OPERADOR)
               VALUES (%s, %s, %s)
               """

        if "Operador Bateladas" in dados:
            for nome in dados["Operador Bateladas"]:
                conn.execute(sql_operador, (tarefa_num, "BATELADA", nome))

        # Se também houver operadores de envase
        if "Operador Envase" in dados:
            for nome in dados["Operador Envase"]:
                conn.execute(sql_operador, (tarefa_num, "ENVASE", nome))


        # 3️⃣ Inserir AMOSTRAS
        sql_amostra = """
        INSERT INTO AMOSTRA_BATELADA (TAREFA_NUM, NUMERO_AMOSTRA)
        VALUES (%s, %s)
        """
        amostras = [(tarefa_num, str(i+1)) for i in range(4)]
        conn.executemany(sql_amostra, amostras)

        # 4️⃣ Inserir MATERIAS-PRIMAS
        materias_primas = dados["Materias primas"]


        # SQL de inserção
        sql_materia = """
            INSERT INTO MATERIA_PRIMA_BATELADA (TAREFA_NUM, NOME, QUANTIDADE, LOTE)
            VALUES (%s, %s, %s, %s)
        """

        # Prepara os valores a serem inseridos
        valores = [
            (tarefa_num, nome, item["Quantidade"], item["Lote"]) for nome, item in materias_primas.items()
        ]
        conn.executemany(sql_materia, valores)

        # ✅ Tudo certo — confirma transação
        conn.commit()
        resultado = True

    except Exception as e:
        print("🚨 Erro detectado:", e)
        conn.rollback()

    finally:
        conn.close()
        return resultado

def get_tarefa(numero_tarefa):
    try:
        conn.connect()
        tarefa_num = numero_tarefa

        # 1️⃣ Consultar dados da BATELADA
        sql_batelada = "SELECT * FROM BATELADA WHERE TAREFA_NUM = %s"
        conn.execute(sql_batelada, (tarefa_num,))
        batelada_rows = conn.cursor.fetchall()
        colunas = conn.cursor.column_names
        bateladas = [dict(zip(colunas, row)) for row in batelada_rows]

        # 2️⃣ Consultar OPERADORES
        sql_operadores = "SELECT * FROM OPERADOR_BATELADA WHERE TAREFA_NUM = %s"
        conn.execute(sql_operadores, (tarefa_num,))
        operador_rows = conn.cursor.fetchall()
        colunas_operadores = conn.cursor.column_names  # nomes das colunas
        operadores = [dict(zip(colunas_operadores, row)) for row in operador_rows]

        # 3️⃣ Consultar AMOSTRAS
        sql_amostras = "SELECT * FROM AMOSTRA_BATELADA WHERE TAREFA_NUM = %s"
        conn.execute(sql_amostras, (tarefa_num,))
        amostra_rows = conn.cursor.fetchall()
        colunas_amostras = conn.cursor.column_names
        amostras = [dict(zip(colunas_amostras, row)) for row in amostra_rows]

        # 4️⃣ Consultar MATERIAS-PRIMAS
        sql_materias = "SELECT * FROM MATERIA_PRIMA_BATELADA WHERE TAREFA_NUM = %s"
        conn.execute(sql_materias, (tarefa_num,))
        materia_rows = conn.cursor.fetchall()
        colunas_materias = conn.cursor.column_names
        materias = [dict(zip(colunas_materias, row)) for row in materia_rows]

        return bateladas, operadores, amostras, materias

    except Exception as e:
        print("🚨 Erro ao consultar dados:", e)


    finally:
        conn.close()


def direciona_gravacao_atualizacao(id_tarefa, dados_json):
    print('estou no direciona')
    if get_tarefa_existe(id_tarefa):
        return update_tarefa(id_tarefa, dados_json)
    else:
        return save_tarefa(dados_json)

def get_tarefa_existe(numero_tarefa):
    try:
        cadastro = False
        conn.connect()
        tarefa_num = numero_tarefa

        sql_check_registro = "SELECT COUNT(*) as total FROM BATELADA WHERE TAREFA_NUM = %s"

        conn.execute(sql_check_registro, (tarefa_num,))
        result = conn.cursor.fetchone()

        if result[0] > 0:
            cadastro = True
        else:
            cadastro = False
        return cadastro


    except Exception as e:
        print("🚨 Erro ao consultar dados:", e)
        return cadastro

    finally:
        conn.close()

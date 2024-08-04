import mysql.connector

class ConexaoBDD:
    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def procura_banco_dados(self, coluna, tabela) -> list:

        conn = mysql.connector.connect(
            host= self.host,
            user= self.user,
            password= self.password,
            database= self.database
        )

        cursor = conn.cursor()
        query = f"SELECT `{coluna[0]}`, `{coluna[1]}` FROM `{tabela}`"

        cursor.execute(query)

        resultado = cursor.fetchall()

        cursor.close()
        
        return resultado
    
    # def printAnalise(self):
    #     texto = f""
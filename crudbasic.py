import mysql.connector
# 1º com a tabela criada no mysql e campos definidos
conexao =mysql.connector.connect(
    host='localhost',
    user='root',
    password='XXXXXXXXX',
    database='bdtestepy',
)
#2º criando o cursor que vai executar os comandos da conexao
cursor = conexao.cursor()


#CREATE
nome_produto = "manga" 
valor = 10
comando = f'INSERT INTO vendas(nome_produto, valor) VALUES("{nome_produto}", {valor})' 
cursor.execute(comando) #mando o comando ser executado
conexao.commit() #editando o banco de dados criado


#READ
comando = f'SELECT * FROM vendas';
cursor.execute(comando) #mando o comando ser executado

resultado = cursor.fetchall() #armazenar informações no cursor e LER
print(resultado)

#UPDATE
nome_produto = "nescau"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"';
cursor.execute(comando) #mando o comando ser executado
conexao.commit()

#DELETE 
nome_produto = "manga"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"';
cursor.execute(comando) #mando o comando ser executado
conexao.commit()



#3º fechando o cursor da conexao
cursor.close()
conexao.close()


from flask import Flask, render_template, request, session, make_response #importando as bibliotecas necessárias
import pymysql #importando a biblioteca pymysql para conexão com o MySQL
app = Flask(__name__) #instanciando a classe Flask

app.secret_key = 's3cr3' #definindo uma chave secreta para a sessão

db = pymysql.connect(host = 'localhost', user = 'root', database = 'usuario') #conectando ao banco de dados MySQL

@app.route('/', methods=['GET', 'POST']) #definindo a rota para a página inicial e permitindo métodos GET e POST

def index():   #função que renderiza a página inicial 
    if request.method == 'GET':# verifica se o método é GET
        if request.cookies.get('usuario'):
            resp = make_response("cookie encontrado, renderizando a página com conteúdo")
        else:
            resp = make_response("nenhum cookie encontrado, renderizando a página sem conteúdo")
            resp.set_cookie('usuario', 'Gabriel')
            
        cursor = db.cursor()  #cria um cursor para executar comandos SQL
        sql = 'SELECT * FROM usuarios'  #comando SQL para selecionar todos os usuarios
        cursor.execute(sql)  #executa o comando SQL
        results = cursor.fetchall()  #executa o comando SQL e obtém todos os resultados
        print(results)  #imprime os resultados no console

        return resp
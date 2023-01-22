#Api criada para consumir documento html (index)

from flask import Flask, render_template #framework utilizado Flask.

app = Flask(__name__) # nome padrão do app por default ele assume o nome da classe.

@app.route("/")  #criação da rota de acesso ao endpoint.
def index(): #ao acessar documento html em Flask uma das opções é utilizar o render_template e adicionar a função index
  return render_template('index.html')

if __name__ == "__main__":
    app.run()






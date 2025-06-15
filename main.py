from flask import Flask, render_template
from src.cardapio import cardapio

app = Flask(__name__)

@app.route('/')
def home():
    
    # A função render_template busca um arquivo na pasta 'templates'
    # e envia variáveis do Python para o HTML.
    # Aqui, estamos enviando nosso dicionário 'cardapio' para o index.html
    return render_template('index.html', cardapio=cardapio)

# Linha necessária para rodar o servidor ao executar o script
if __name__ == '__main__':
    app.run(debug=True) # debug=True ajuda a ver erros e atualiza o servidor automaticamente
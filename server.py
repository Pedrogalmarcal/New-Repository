from flask import Flask, request, jsonify
import os
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def receber_dados():
    dados = request.get_json()
    print("Dados recebidos:", dados)
    return jsonify({"status": "sucesso", "dados_recebidos": dados})


@app.route('/')
def home():
    return "Servidor rodando!", 200


@app.route('/')
def get_url():
    url = os.environ.get('RAILWAY_URL', 'URL não encontrada')
    return f"Sua URL é: {url}"


if __name__ == '__main__':
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

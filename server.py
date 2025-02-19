from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def receber_dados():
    dados = request.get_json()
    print("Dados recebidos:", dados)
    return jsonify({"status": "sucesso", "dados_recebidos": dados})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

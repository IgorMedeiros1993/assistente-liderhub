from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # Verifica se veio mensagem
    if data and "mensagem" in data:
        mensagem = data["mensagem"].strip()

        if mensagem == "5":
            # Resposta automática quando o cliente digitar "5"
            resposta = {
                "mensagem": "\u2728 Olá! Sou o Assistente Virtual! Vamos começar?\n\nPor favor, me diga seu nome completo:"
            }
            return jsonify(resposta)

    # Se não for o "5", não faz nada
    return jsonify({})

@app.route("/", methods=["GET"])
def home():
    return "Assistente está online!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

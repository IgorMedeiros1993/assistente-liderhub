from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # Ajuste: pegar a mensagem do jeito que o LiderHub manda
    mensagem = ""
    if data:
        if isinstance(data.get("mensagem"), dict):
            mensagem = data["mensagem"].get("conteudo", "").strip()
        elif isinstance(data.get("mensagem"), str):
            mensagem = data["mensagem"].strip()

    # Agora sim: se o cliente mandou "5"
    if mensagem == "5":
        resposta = {
            "mensagem": "✨ Olá! Sou o Assistente Virtual! Vamos começar?\n\nPor favor, me diga seu nome completo:"
        }
        return jsonify(resposta)

    # Se não for "5", não faz nada
    return jsonify({})

@app.route("/", methods=["GET"])
def home():
    return "Assistente está online!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

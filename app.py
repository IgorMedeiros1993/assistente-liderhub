from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    # Captura a mensagem recebida
    mensagem = data.get('mensagem', '').strip()

    if mensagem == "5":
        # Cliente escolheu falar com o assistente
        resposta = "Ótimo! Vamos iniciar seu atendimento. 😊\n\nPor favor, me diga seu nome completo:"
    elif mensagem in ["1", "2", "3", "4"]:
        # Cliente escolheu outra opção
        resposta = "Perfeito! Vou te direcionar para o setor responsável. 🧑‍💼"
    else:
        # Se digitar outra coisa
        resposta = "Desculpe, não entendi. Por favor, responda com o número da opção desejada. 😊"

    return jsonify({"resposta": resposta})

if __name__ == '__main__':
    app.run()

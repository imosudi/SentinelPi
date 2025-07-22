from flask import Flask, request
import telebot
import os

app = Flask(__name__)

# Initialize the Telegram bot with the token from environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    message = data.get('message', 'No message provided')
    chat_id = data.get('chat_id')

    if chat_id:
        bot.send_message(chat_id, message)
        return {'status': 'success', 'message': 'Alert sent'}, 200
    else:
        return {'status': 'error', 'message': 'Chat ID not provided'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  # Run on a different port to avoid conflicts with Flask UI
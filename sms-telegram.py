from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/incoming-sms', methods=['POST'])
def incoming_sms():
    data = request.form
    sms_body = data.get('message')
    sender = data.get('from')

    # Telegram API URL
    telegram_api_url = f'https://api.telegram.org/{YOUR_BOT_API}/sendMessage'
    
    # Create a payload for Telegram
    payload = {
        'chat_id': '{YOURID}',
        'text': f'New SMS from {sender}: {sms_body}'
    }

    # Forward the SMS to Telegram
    response = requests.post(telegram_api_url, json=payload)

    if response.status_code == 200:
        return "SMS forwarded to Telegram successfully 🚀"
    else:
        return f"Failed to forward SMS to Telegram. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

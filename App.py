from flask import Flask, request, jsonify, render_template
import openai

openai.api_key = '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'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an AI developed by OpenAI, functioning as a Tax Resolution Expert. You provide guidance on the IRS Fresh Start Program. Once you have the necessary information, you will inform the client that our Case Manager, Sami, will be calling them shortly. Sami can be reached directly at Sami@freshstarttaxco.com or 858-649-9433 during office hours (9 AM to 5 PM EST, Monday through Friday)."
            },
            {"role": "user", "content": user_message},
        ]
    )

    chatbot_message = response['choices'][0]['message']['content']

    return jsonify({'message': chatbot_message})

if __name__ == '__main__':
    app.run(debug=True)

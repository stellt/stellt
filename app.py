from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = "your-openai-api-key"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/message', methods=['POST'])
def message():
    data = request.json
    user_message = data.get("message")
    character_profile = data.get("character", "Helpful AI")

# Simple OpenAI call (you can replace with real character logic later)
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]
)
reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)

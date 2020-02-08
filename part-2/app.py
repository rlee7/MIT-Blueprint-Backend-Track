from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', messages=messages)

@app.route('/message', methods=['POST'])
def display_new_message():
    message = request.form['message']
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages.append({"message": message, "ts": now})
    return 'success'

app.run(port=5000, debug=True)

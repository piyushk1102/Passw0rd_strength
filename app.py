from flask import Flask, render_template, request
from password_tool import analyze_password, generate_password
from collections import deque

app = Flask(__name__)

# Store the last 5 generated passwords in a simple history
password_history = deque(maxlen=5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    strength, entropy, feedback = analyze_password(password)
    return render_template('index.html', password=password, strength=strength, entropy=entropy, feedback=feedback)

@app.route('/generate_password', methods=['POST'])
def generate_password_view():
    length = int(request.form['length'])
    include_uppercase = 'uppercase' in request.form
    include_digits = 'digits' in request.form
    include_special = 'special' in request.form
    
    generated_password = generate_password(length, include_uppercase, include_digits, include_special)
    password_history.appendleft(generated_password)  # Store in history
    
    return render_template('index.html', generated_password=generated_password, password_history=password_history)

if __name__ == '__main__':
    app.run(debug=True)
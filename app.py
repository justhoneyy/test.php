from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    # Log credentials (simulation only!)
    with open("creds.txt", "a") as f:
        f.write(f"Email: {email}, Password: {password}\n")
    return "This was a phishing simulation. Credentials logged for demo only."

if __name__ == "__main__":
    app.run()

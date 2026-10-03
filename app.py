from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        event = request.form["event"]

        return f"""
        <h1>Registration Successful!</h1>
        <p>Thank you, {name}.</p>
        <p>Email: {email}</p>
        <p>Phone: {phone}</p>
        <p>Event: {event}</p>
        """

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
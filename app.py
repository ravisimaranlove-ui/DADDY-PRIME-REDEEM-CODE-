from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "daddyprime_secret_key"

SAMPLE_CODES = [
    ("₹10 Drop (IND)", "DPIND9K21L4M5N6P", "Active"),
    ("₹50 Drop (IND)", "IND50XYZ98A1B2C3", "Active"),
    ("₹100 Drop (IND)", "FREE88IND4567890", "Active"),
    ("₹500 Drop (IND)", "DP500PLAY9988IND", "Active"),
    ("₹1000 Mega Drop", "IND1000VIP998877", "Active"),
    ("₹5000 Grand Drop", "DP5000LUCKIND777", "Active")
]

@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", user=session["user"], codes=SAMPLE_CODES)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "Gamer")
        session["user"] = username
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

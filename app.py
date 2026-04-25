from flask import Flask, render_template, request

app = Flask(__name__)

registrations = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        registrations.append({"name": name, "email": email})
    return render_template("index.html", data=registrations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
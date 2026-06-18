from flask import Flask, render_template
import json

app = Flask(__name__)

with open("data/riders.json", encoding="utf-8") as file:
    riders = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/riders")
def show_riders():
    return render_template(
        "riders.html",
        riders=riders
    )

@app.route("/rider/<int:id>")
def rider_detail(id):

    rider = next(
        (r for r in riders if r["id"] == id),
        None
    )

    return render_template(
        "detail.html",
        rider=rider
    )

if __name__ == "__main__":
    app.run(debug=True)
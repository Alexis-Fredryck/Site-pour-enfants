from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/iconographies")
def iconographies():
    return render_template("Iconographies.html")  # affiche Iconographies.html

if __name__ == "__main__":
    app.run(debug=True)

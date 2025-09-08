from flask import Flask, render_template,request
import requests 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/iconographies")
def iconographies():
    return render_template("Iconographies.html") 


@app.route("/ask", methods=["GET", "POST"])
def ask():
    answer = None
    if request.method == "POST":
        question = request.form["question"]
        
        # Appel à l'API locale d'Ollama
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": question,
                "stream": False
            }
        )
        
        answer = response.json()["response"]

        return render_template("ask.html", question=question, answer=answer)

    return render_template("ask.html", question=None, answer=None)


if __name__ == "__main__":
    app.run(debug=True)

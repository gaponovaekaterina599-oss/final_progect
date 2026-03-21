from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print("LOL")


if __name__ == "__main__":
    app.run()

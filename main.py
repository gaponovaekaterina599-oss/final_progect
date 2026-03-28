from flask import Flask
from flask import render_template, request

app = Flask(__name__)
user = []





@app.route('/', methods=['GET', 'POST', ])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print('post')
        print(request.form.get('user_input'),user.append())
        return render_template("index.html")

if __name__ == "__main__":
    app.run()

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
        print(user.append(request.form.get('user_input')))
        return render_template("index.html")



if __name__ == "__main__":
    app.run()


#Todo сделать ссылку на второстепенную страницу https://doka.guide/html/a/
#Todo сделать стилизациювторостпеной страницы

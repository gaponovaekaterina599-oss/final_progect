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


# Todo 1 сделать страницу html css с задачами (Пример: 1 - задача 1
#                                                      2 - задача 2)

# Todo 2 user передавать на стрницу html с помощью for выводить данные (урок 20)

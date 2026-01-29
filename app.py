#import random
#from flask import Flask, render_template, url_for, redirect, request

#app = Flask(__name__)

#@app.route('/')
#def home():
#    return render_template("test.html")



#@app.route('/', methods=['POST'])
#def page():
  #  print(239)
  #  if request.method == 'POST':
  #      return redirect(url_for('newPage'))

#@app.route('/newPage')
#def newPage():
   # return render_template("newPage.html")

#if __name__ == '__main__':
  #  app.run(debug=True)

    # return render_template("newPage.html")
import random
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # Разрешаем оба метода здесь
def home():
    if request.method == 'POST':
        print(239)
        return redirect(url_for('newPage'))

    # Если это обычный заход на страницу (GET):
    random_path = [
        {'x': random.randint(0, 85), 'y': random.randint(0, 85)}
        for _ in range(5)
    ]
    return render_template("test.html", path=random_path)


@app.route('/newPage')
def newPage():
    return render_template("newPage.html")


if __name__ == '__main__':
    app.run(debug=True)

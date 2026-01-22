from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("test.html")


@app.route('/', methods=['POST'])
def page():
    print(239)
    if request.method == 'POST':
        return redirect(url_for('newPage'))

@app.route('/newPage')
def newPage():
    return render_template("newPage.html")

if __name__ == '__main__':
    app.run(debug=True)

    # return render_template("newPage.html")
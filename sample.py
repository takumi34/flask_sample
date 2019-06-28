from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hi():
    return "hi"

@app.route('/sample/')
@app.route('/sample/<name>')
def hihi(name=None):
    return render_template('sample.html', name=name)

if __name__ == '__main__':
    app.run()

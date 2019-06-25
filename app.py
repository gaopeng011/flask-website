from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    # return "hello flask!"
    title = "Home"
    paragraphs = [
        'section 1',
        'section 2',
        'section 3',
    ]
    return render_template("index.html", title=title, data=paragraphs)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
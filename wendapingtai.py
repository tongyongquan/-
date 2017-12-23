#encoding: utf-8

from exts import db
from flask import Flask
import config
from flask import render_template

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

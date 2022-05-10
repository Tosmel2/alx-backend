#!/usr/bin/env python3

"""
Parametrize templates
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    make configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    get locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """
    return string
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/env python3
"""
Flask application with Babel configuration.

This module sets up a Flask app with Flask-Babel
to support internationalization.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask app.

    Defines available languages and default locale settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Render the index page.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

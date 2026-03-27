#!/usr/bin/env python3
"""
Flask application module with Babel localization support.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask-Babel.

    Attributes:
        LANGUAGES (list): Supported languages ('en' and 'fr').
        BABEL_DEFAULT_LOCALE (str): Default language for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Create Flask application
app = Flask(__name__)

# Load configuration from Config class
app.config.from_object(Config)

# Create Babel object linked to the Flask app
babel = Babel()


def get_locale() -> str:
    """
    Determine the best matching language for the current request.

    Checks for a 'locale' query parameter in the URL. If provided and valid,
    it will override the default. Otherwise, uses the request's Accept-Language header.

    Returns:
        str: Selected locale code ('en' or 'fr').
    """
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


# Initialize Babel with the locale selector
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """
    Render the main page template.

    Returns:
        str: Rendered HTML from '4-index.html'.
    """
    return render_template("4-index.html")


# Run the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/env python3
"""
Flask application module with Babel localization and simulated user support.

This module sets up a Flask app with language detection using Flask-Babel.
It supports user-specific locales, URL query parameters, and default browser
languages.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask-Babel and supported languages.

    Attributes:
        LANGUAGES (list): Supported language codes ('en', 'fr').
        BABEL_DEFAULT_LOCALE (str): Default language for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
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

# Simulated users table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieve the currently logged-in user
    based on the 'login_as' query parameter.

    Checks if 'login_as' is provided in the URL and corresponds to a user
    in the simulated users table. Returns the user dictionary if found,
    otherwise returns None.

    Returns:
        dict or None: User data if a valid user is found, else None.
    """
    user_id = request.args.get("login_as")
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        if user_id in users:
            return users[user_id]
    return None


def get_locale() -> str:
    """
    Determine the best matching language for the current request.

    The priority order is as follows:
        If a 'locale' query parameter is provided in the URL
        and is supported, it is used.
        If a user is logged in and their locale is supported, it is used.
        Otherwise, the best match from the request's
        Accept-Language headers is used.

    Returns:str: Selected locale code ('en' or 'fr').
    """
    # Priority 1: Check 'locale' query parameter
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale

    # Priority 2: Check logged-in user's locale
    user = get_user()
    if user and user["locale"] in Config.LANGUAGES:
        return user["locale"]

    # Priority 3: Use Accept-Language header
    return request.accept_languages.best_match(Config.LANGUAGES)


# Initialize Babel with the locale selector
babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """
    Hook executed before each request.

    Sets the global `g.user` variable to the currently logged-in user.
    """
    g.user = get_user()


@app.route("/")
def index():
    """
    Render the main page template.

    Returns:
        str: Rendered HTML from '6-index.html'.
    """
    return render_template("6-index.html")


# Run the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/env python3
"""
Flask application module with Babel localization and user time zone support.

This module sets up a Flask app with language and time zone detection using
Flask-Babel. It supports user-specific locales and time zones, URL query
parameters, and defaults to UTC for unknown time zones.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional
import pytz
from pytz.exceptions import UnknownTimeZoneError


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
app.config.from_object(Config)
babel = Babel()

# Simulated users table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[dict]:
    """
    Retrieve the currently logged-in user based on 'login_as' query parameter.

    Returns:
        dict or None: User data if valid user found, else None.
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

    Priority order:
        1. 'locale' query parameter if provided and supported.
        2. Logged-in user's locale if supported.
        3. Best match from Accept-Language header.

    Returns:
        str: Selected locale code ('en' or 'fr').
    """
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale

    user = get_user()
    if user and user["locale"] in Config.LANGUAGES:
        return user["locale"]

    return request.accept_languages.best_match(Config.LANGUAGES)


def get_timezone() -> str:
    """
    Determine the best matching time zone for the current request.

    Priority order:
        1. 'timezone' query parameter if provided and valid.
        2. Logged-in user's timezone if valid.
        3. Default to UTC.

    Returns:
        str: Selected time zone.
    """
    tzname = request.args.get("timezone")
    if tzname:
        try:
            pytz.timezone(tzname)
            return tzname
        except UnknownTimeZoneError:
            pass

    user = get_user()
    if user and user.get("timezone"):
        try:
            pytz.timezone(user["timezone"])
            return user["timezone"]
        except UnknownTimeZoneError:
            pass

    return "UTC"


# Initialize Babel with custom locale and timezone selectors
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.before_request
def before_request() -> None:
    """
    Hook executed before each request.

    Sets the global `g.user` variable to the currently logged-in user.
    """
    g.user = get_user()


@app.route("/")
def index() -> str:
    """
    Render the main page template.

    Returns:
        str: Rendered HTML from '7-index.html'.
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

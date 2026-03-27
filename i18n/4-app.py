#!/usr/bin/env python3
"""
4-app.py
Flask app that supports forcing locale with URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

@babel.localeselector
def get_locale():
    """Determine the best match with supported languages."""
    # Check if 'locale' parameter exists in the URL
    locale = request.args.get('locale')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    # Fallback to default behavior (e.g., Accept-Language)
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/', strict_slashes=False)
def index():
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

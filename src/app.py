"""
Main module for the Flask greeting application.
This module sets up the Flask app and defines the routes.
"""

import random
from flask import Flask

app = Flask(__name__)

GREETINGS = [
    "Hello, World!",
    "¡Hola Mundo!",
    "Bonjour le monde!",
    "Hallo Welt!",
    "Ciao Mondo!",
    "Zdravey, Svyat!",
]


@app.route("/")
def hello():
    """
    Selects a random greeting from the list and returns it.
    """
    # Using random for greetings is safe, not used for cryptography.
    selected_greeting = random.choice(GREETINGS)  # nosec
    return f"{selected_greeting}"


if __name__ == "__main__":
    # Binding to 0.0.0.0 is required for Docker container access.
    app.run(debug=False, host="0.0.0.0", port=5000)  # nosec

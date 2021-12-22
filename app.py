from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def alive_response():
    """Basic REST response function. Returns something if app is alive"""
    return "App is alive!"

@app.route("/chat")
def parse_tg_message()->str:
    """Telegram message requests responder"""
    # TODO
    return "This should be message"

@app.route("/invoke/<user_id>")
def invoke_asker(user_id: str)->str:
    """Internal invoking method"""
    return f"This should be another message id is {escape(user_id)}"
    
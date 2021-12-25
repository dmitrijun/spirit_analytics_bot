from flask import Flask, request, abort
from markupsafe import escape
import os

from tg_bot.webhook_handler import UpdateHandler

app = Flask(__name__)


@app.route("/", methods=["GET"])
def alive_response():
    """Basic REST response function. Returns something if app is alive"""
    return "App is alive!"


@app.route("/chat", methods=["POST"])
def parse_tg_message() -> str:
    """Telegram message requests responder"""
    try:
        request_data = request.get_json(force=True)
        bot = UpdateHandler(request_data, os.environ["tg_bot_token"])
        bot.do_something()
        return "Successfull"
    except Exception as e:
        abort(500)

@app.route("/invoke/<user_id>", methods=["GET"])
def invoke_asker(user_id: str) -> str:
    """Internal invoking method"""
    return f"This should be another message id is {escape(user_id)}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

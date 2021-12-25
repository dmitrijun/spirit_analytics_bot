#encoding utf-8
"""
    Wholesome telegram update handler
"""
import random
import os

from telegram import Bot


class UpdateHandler():
    def __init__(self, update_json: dict, bot_token: str):
        try:
            self.bot = Bot(bot_token)
            self.text = update_json["message"]["text"]
            self.chat_id = update_json["message"]["chat"]["id"]
        except Exception: # pylint: disable=broad-except
            pass

    def do_something(self):
        """
            Sending random citate now
        """
        try:
            reply_text = "I do not care what you've just sent :^).\n"
            with open(os.path.join("sources", "citaites.txt"), "r", encoding="utf-8") as file:
                allText = file.read()
                lines = allText.split('\n')
                reply_text += "But here's a citate for u: \n"
                reply_text += random.choice(lines)

            self.bot.send_message(
                chat_id=self.chat_id, text=reply_text)
            return reply_text
        except Exception: # pylint: disable=broad-except
            pass

import logging

from telegram import Bot


class UpdateHandler():
    def __init__(self, update_json: dict, bot_token: str):
        try:
            logging.info(f"Initializing Handler: {update_json}")
            self.bot = Bot(bot_token)
            self.text = update_json["message"]["text"]
            self.chat_id = update_json["message"]["chat"]["id"]
            # logging.info(f"Got new message with text: '{self.update_object.message.text}'")
        except Exception as e:
            logging.error(f"Init unsuccessfull {e}")
            raise ValueError()

    def do_something(self):
        try:
            # logging.debug(f"Sending message to {self.update_object.effective_chat.id}")
            self.bot.send_message(
                chat_id=self.chat_id, text="I do not care what you've just sent :^).")
            # logging.info(f"Message successfully sent to{self.update_object.effective_chat.id}")
        except Exception as e:
            logging.error(f"Unable to send message: {e}")

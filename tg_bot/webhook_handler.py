from telegram import update, Bot

class UpdateHandler():
    def __init__(self, update_json:dict):
        try:
            self.bot = Bot("token_goes_here")
            self.update_object = update.de_json(update_json, self.bot)
        except: 
            raise ValueError()

    def do_something(self):
        self.bot.send_message(chat_id=self.update_object.effective_chat.id, text="I do not care what you've just sent :^).")
import telegram

class Telebot:
    def __init__(self):
        """TODO Config - bot_token e chat_id em arquivo de config"""
        self.bot_token = '1481769455:AAGV1Hx7EA4eje9OUVCtbpLNlg4xgsbzZq8'
        self.chat_id   = '-418626952'
        self.bot = telegram.Bot(token=self.bot_token)

    def send_text_msg(self, msg):
        return self.bot.sendMessage(chat_id=self.chat_id, text=msg)

    def send_photos(self, photos):
        return self.bot.send_media_group(chat_id=self.chat_id, media=photos, disable_notification=True)
        #return self.bot.send_photo(chat_id=self.chat_id, photo=open(photo, 'rb'))
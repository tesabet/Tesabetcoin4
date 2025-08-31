from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = "8497680999:AAHclqnExmf1FsIlptHPalXnEC5zlxFHMtY"
GAME_SHORT_NAME = "rise_of_tesabet"

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Start ▶️", callback_game=GAME_SHORT_NAME)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("🎮 Rise of Tesabet’e Hoş Geldin! Başlamak için tıkla.", reply_markup=reply_markup)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
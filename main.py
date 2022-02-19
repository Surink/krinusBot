import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    origen = datetime.strptime("9/9/2021 21:09:09", "%m/%d/%Y %H:%M:%S")
    ahora = datetime.now()
    lapso = ahora - origen

    plantilla = "Todo eso está muy bien. Pero deberíais centraros en que lleváis {} dias, {} horas, {} minutos y {} segundos saliendo. Pareja del año!"

    segundos = lapso.total_seconds()

    minutos = segundos // 60
    segundos = int(segundos % 60)

    horas = minutos // 60
    minutos = int(minutos % 60)

    dias = int(horas // 24)
    horas = int(horas % 24)

    update.message.reply_text(plantilla.format(dias, horas, minutos, segundos))


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5173523414:AAHOR4WvtibTDTzW_lQK6Xc9DGksi9V5Rec")

    # Get the dispatcher to register handlers jk
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
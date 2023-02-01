from telegram import Bot
from bot import convos
import config
from log import logger
from bot import commands
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    Dispatcher,
    ConversationHandler,
)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def prepare_dispatcher(dp):
    # conversations (must be declared first, not sure why)
    convo_text_filter = Filters.text & (
        ~Filters.text(["/cancel", "/cancel@scheduler_telebot"])
    )
    dp.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("pollday", commands.poll_day)],
            states={
                convos.state0: [MessageHandler(convo_text_filter, convos.choose_week)],
                convos.state1: [MessageHandler(convo_text_filter, convos.send_poll)],
            },
            fallbacks=[CommandHandler("cancel", commands.cancel_convo)],
        )
    )

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", commands.start))
    dp.add_handler(CommandHandler("help", commands.help))
    dp.add_handler(CommandHandler("cancel", commands.cancel))

    # log all errors
    dp.add_error_handler(error)


# Use webhook when running in prod (via gunicorn)
if config.ENV:
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    bot.setWebhook(config.BOTHOST)
    dp = Dispatcher(bot=bot, update_queue=None)
    prepare_dispatcher(dp)


# Use polling when running locally
if __name__ == "__main__":
    updater = Updater(config.TELEGRAM_BOT_TOKEN, use_context=True)
    updater.stop()
    updater.is_idle = False

    dp = updater.dispatcher
    prepare_dispatcher(dp)
    updater.start_polling()
    updater.idle()

    # Used for testing webhook locally, instructions for how to set up local webhook at https://dev.to/ibrarturi/how-to-test-webhooks-on-your-localhost-3b4f
    # app.run(debug=True)

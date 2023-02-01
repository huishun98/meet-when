from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode

# custom messages
start_message = "<b>Thank you for using Meet When?</b>\n\n/pollday to start "  # html
help_message = 'I can help you create polls for meetups.\n\n<b>Available commands</b>\n/pollday - Poll for day of week\n\n<b>Found a bug?</b>\nPlease contact the bot owner at <a href="http://mailto:hs.develops.2@gmail.com/">hs.develops.2@gmail.com</a>.\n\n<b>Enjoying the bot?</b>\nYou can <a href="https://www.buymeacoffee.com/hschua">buy the me a coffee</a>!'  # html
no_convo_message = "No convo to cancel"

convo_postfix = "\n\n/cancel to end this convo."
convo_state0_message = "Meeting in which month?" + convo_postfix
convo_state1_message = "Which week (Sat to following Sun)?" + convo_postfix
convo_ended_message = "Convo ended"
error_message = "Invalid input." + convo_postfix
exceed_limit_error_message = "Too many days! (max. 31 days)" + convo_postfix


def send_start_message(update):
    update.message.reply_text(text=start_message, parse_mode=ParseMode.HTML)


def send_help_message(update):
    update.message.reply_text(
        help_message, parse_mode=ParseMode.HTML, disable_web_page_preview=True
    )


def send_convo_ended_message(update):
    update.message.reply_text(convo_ended_message, reply_markup=ReplyKeyboardRemove())


def send_convo_state0_message(update, keyboard):
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )
    update.message.reply_text(convo_state0_message, reply_markup=reply_markup)


def send_convo_state1_message(update, keyboard):
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )
    update.message.reply_text(convo_state1_message, reply_markup=reply_markup)


def send_error_message(update):
    update.message.reply_text(error_message)


def send_exceed_limit_error_message(update):
    update.message.reply_text(exceed_limit_error_message)


def send_poll(update, context, question, answers):
    context.bot.send_poll(
        update.effective_chat.id,
        question,
        answers,
        is_anonymous=False,
        allows_multiple_answers=True,
        reply_markup=ReplyKeyboardRemove(),
    )


def send_no_convo_message(update):
    update.message.reply_text(no_convo_message)

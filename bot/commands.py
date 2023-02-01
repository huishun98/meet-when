from bot import replies, convos
from telegram.ext import ConversationHandler
import calendar
from datetime import datetime
from bot import utils


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, _):
    """Send a message when the command /start is issued."""
    # timezone must be defined in order to create new job
    replies.send_start_message(update)


def help(update, _):
    """Send a message when the command /help is issued."""
    replies.send_help_message(update)


def poll_day(update, _):
    """Send a message when the command /pollday is issued."""

    suggestions = []

    month = datetime.now().month - 1
    year = datetime.now().year
    for i in range(month, (month + 10)):
        month_name_i = i % 12 + 1
        suggestion = "%s %s" % (calendar.month_name[month_name_i], year)
        suggestions.append(suggestion)
        if month_name_i == 12:
            year = year + 1

    keyboard = utils.prepare_keyboard(suggestions)
    replies.send_convo_state0_message(update, keyboard)
    return convos.state0


def cancel_convo(update, _):
    """Send a message when the command /cancel is issued."""
    replies.send_convo_ended_message(update)
    return ConversationHandler.END


def cancel(update, _):
    """Send a message when the command /cancel is issued."""
    replies.send_no_convo_message(update)

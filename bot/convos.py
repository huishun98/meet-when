import re
import calendar
from bot import replies, utils
from datetime import datetime, timedelta
from telegram.ext import ConversationHandler

state0, state1 = range(2)


# state 0
def choose_week(update, _):
    year = datetime.now().year
    regex = (
        r"^(January|February|March|April|May|June|July|August|September|October|November|December) (%s|%s)$"
        % (year, year + 1)
    )

    match = re.search(regex, str(update.message.text))
    if match is None:
        replies.send_error_message(update)
        return state0

    month_name, year = match.group(1, 2)
    month = list(calendar.month_name).index(month_name)
    year = int(year)

    suggestions = []

    start_date = utils.first_monday_of_month(year, month) - timedelta(2)
    end_date = start_date + timedelta(8)

    if end_date.month == start_date.month and start_date.day != 1:
        start_date = start_date - timedelta(7)
        end_date = start_date + timedelta(8)

    for i in range(6):
        start_string = start_date.strftime("%d/%m")
        end_string = end_date.strftime("%d/%m")
        suggestions.append("%s — %s" % (start_string, end_string))
        if i > 1 and start_date.month < end_date.month:
            break
        start_date = end_date - timedelta(1)
        end_date = start_date + timedelta(8)

    keyboard = utils.prepare_keyboard(suggestions)
    replies.send_convo_state1_message(update, keyboard)
    return state1


# ref: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/pollbot.py
def send_poll(update, context):
    regex = r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1])\/(0[1-9]|1[0-2]) — (0[1-9]|1[0-9]|2[0-9]|3[0-1])\/(0[1-9]|1[0-2])$"
    match = re.search(regex, str(update.message.text))

    if match is None:
        replies.send_error_message(update)
        return state1

    now = datetime.now()
    curr_year = now.year

    day1, month1, day2, month2 = match.group(1, 2, 3, 4)
    day1, month1, day2, month2 = int(day1), int(month1), int(day2), int(month2)

    try:
        date1 = datetime(curr_year, month1, day1)
        date2 = datetime(curr_year, month2, day2)
        if date1.date() < now.date():
            date1 = datetime(curr_year + 1, month1, day1)
        if date2.date() < date1.date() or date2.date() < now.date():
            date2 = datetime(curr_year + 1, month2, day2)
    except:
        replies.send_error_message(update)
        return state1

    answers = []

    if (date2 - date1).days > 31:
        replies.send_exceed_limit_error_message(update)
        return state1

    date = date1
    while date.date() <= date2.date():
        day_of_week = calendar.day_name[date.weekday()]
        answer = "%s (%s)" % (date.strftime("%d/%m"), day_of_week)
        answers.append(answer)
        date = date + timedelta(1)

    replies.send_poll(update, context, "Available dates", answers)
    return ConversationHandler.END

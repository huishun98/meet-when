from datetime import datetime, timedelta
import numpy as np


def first_monday_of_month(year, month):
    d = datetime(year, month, 7)
    offset = -d.weekday()  # weekday = 0 means monday
    return d + timedelta(offset)


def prepare_keyboard(suggestions):
    return np.split(np.array(suggestions), np.arange(2, len(suggestions), 2))

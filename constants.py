"""
The constant variables are made to have to change only one digit and
avoid any errors.
"""
from datetime import date
from datetime import timedelta


NUMBER_OF_DAY = 0
NUMBER_OF_ROUND = 4
NUMBER_OF_PLAYERS = 8

START_DATE = date.today()
END_DATE = START_DATE + timedelta(NUMBER_OF_DAY)

#!/usr/bin/env python3

from datetime import datetime
from datetime import date
import time
import os


def new_pomodoro():
    total_pom_minutes = 25
    total_pom_seconds = total_pom_minutes * 60
    time.sleep(total_pom_seconds)
    os.system('say "Your pomodoro is completed"')


def alexa_pomodoro():
    os.system('say "Alexa, set timer for 25 minutes"')


def is_it_pycon():
    pycon_start_date = date(2018, 5, 19)
    pycon_end_date = date(2018, 5, 17)
    todaydate = date.today()

    if pycon_start_date <= todaydate <= pycon_end_date:
        print("it's Pycon2018 Baby!!!!")
    else:
        if todaydate > pycon_end_date:
            print("You missed Pycon, try next year")
        else:
            print("There are still " + str((pycon_start_date - todaydate).days) + " days until Pycon2018")
            print("I guess I will code in the meantime.  Let's do a pomodoro")
            #new_pomodoro()
            alexa_pomodoro()

is_it_pycon()

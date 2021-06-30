from os import waitpid
from typing import Dict
import json as _json
import datetime as _dt

def get_all_events() -> Dict:
    with open("events.json", encoding='utf-8') as events_file:
        data = _json.load(events_file)
    
    return data

def get_all_events_of_interest() -> Dict:
    with open("events_of_interest.json", encoding='utf-8') as events_of_interest_file:
        data = _json.load(events_of_interest_file)

    return data

def get_month_events(month: str) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "This month isn't real"

def get_month_events_of_interest(month: str) -> Dict:
    events = get_all_events_of_interest()
    month = month.lower()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "This month isn't real"

def get_events_of_day(month: str, day: int) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        events = events[month][str(day)]
        return events
    except KeyError:
        return "What is wrong with you"

def get_events_of_interest_of_day(month: str, day: int) -> Dict:
    events = get_all_events_of_interest()
    month = month.lower()
    try:
        events = events[month][str(day)]
        return events
    except KeyError:
        return "What is wrong with you"

def get_today_events():
    today = _dt.date.today()
    month = today.strftime("%B")
    return get_events_of_day(month, today.day)

def get_today_events_of_interest():
    today = _dt.date.today()
    month = today.strftime("%B")
    return get_events_of_interest_of_day(month, today.day)

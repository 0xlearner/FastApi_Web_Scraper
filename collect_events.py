from typing import Iterator, Dict
import datetime as _dt
import json as _json

import scraper as _scraper

def _date_range(start_date: _dt.date, end_date: _dt.date) -> Iterator[_dt.date]:
    for n in range(int ((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n)

def create_events_dict() -> Dict:
    events = dict()
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2021, 1, 1)

    for date in _date_range(start_date, end_date):
        month =  date.strftime("%B").lower()
        if month not in events:
            events[month] = dict()
        events[month][date.day] = _scraper.events_of_the_day(month, date.day)
    
    return events

def create_events_of_interest_dict() -> Dict:
    event_of_interest = dict()
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2021, 1, 1)

    for date in _date_range(start_date, end_date):
        month =  date.strftime("%B").lower()
        if month not in event_of_interest:
            event_of_interest[month] = dict()
        event_of_interest[month][date.day] = _scraper.events_of_interest(month, date.day)
    
    return event_of_interest

if __name__ == '__main__':
    events = create_events_dict()
    with open("events.json", "w", encoding='utf-8') as events_file:
        _json.dump(events, events_file, ensure_ascii=False)

    event_of_interest = create_events_of_interest_dict()
    with open("events_of_interest.json", "w", encoding='utf-8') as events_of_interest_file:
        _json.dump(event_of_interest, events_of_interest_file, ensure_ascii=False)
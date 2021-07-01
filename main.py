from fastapi import FastAPI
import starlette.responses as  _responses

import services as _service

app = FastAPI()

@app.get("/")
async def root():
    return _responses.RedirectResponse("/docs")

@app.get("/events")
async def all_events():
    return _service.get_all_events()

@app.get("/events/today")
async def events_of_day():
    return _service.get_today_events()

@app.get("/events_of_interest")
async def all_events():
    return _service.get_all_events_of_interest()

@app.get("/events_of_interest/today")
async def events_of_day():
    return _service.get_today_events_of_interest()


@app.get("/events/{month}")
async def get_events_of_month(month: str):
    return _service.get_month_events(month)

@app.get("/events_of_interest/{month}")
async def get_events_of_month(month: str):
    return _service.get_month_events_of_interest(month)

@app.get("/events/{month}/{day}")
async def events_of_day(month: str, day: int):
    return _service.get_events_of_day(month, day)

@app.get("/events_of_interest_of_day/{month}/{day}")
async def events_of_day(month: str, day: int):
    return _service.get_events_of_interest_of_day(month, day)
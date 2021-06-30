from typing import List
import requests as _requests
import bs4 as _bs4

def _generate_url(month: str, day: int) -> str:
    url = f'https://www.onthisday.com/events/{month}/{day}'
    return url

def _get_page(url: str) -> _bs4.BeautifulSoup:
    _page = _requests.get(url)
    soup = _bs4.BeautifulSoup(_page.content, 'html.parser')
    return soup

def events_of_the_day(month: str, day: int) -> List[str]:
    """
    Return the events of a given day
    """
    url = _generate_url(month, day)
    events = []
    
    while True:
        page = _get_page(url)
        for event in page.select('li.event'):
            events.append(event.text)
        next_link = page.select_one('a.pag__next')
        if not next_link:
            break
        url = 'https://www.onthisday.com'+next_link['href']
    
    return events

def events_of_interest(month: str, day: int) -> List[str]:
    """
    Return the event of interest of a given day
    """
    url = _generate_url(month, day)
    event_of_interest = []
    
    while True:
        page = _get_page(url)
        for event in page.find_all('div', class_='section--person-of-interest'):
            event_of_interest.append(' '.join(event.text.split()))
        next_link = page.select_one('a.pag__next')
        if not next_link:
            break
        url = 'https://www.onthisday.com'+next_link['href']
    
    return event_of_interest
    

# events_of_the_day("february", 5)
# events_of_interest("february", 5)
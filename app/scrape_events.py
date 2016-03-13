import requests
import datetime
import database
import models


TOURISM_VICTORIA_EVENTS_ENDPOINT = "https://www.eventbrite.ca/directory/json?page={}&cat=&format=&q=victoria+bc&loc=Victoria%2C+BC%2C+Canada&date=&start_date=&end_date=&is_paid=&sort=best&crt=regular&slat=&slng=&radius=&vp_ne_lat=&vp_ne_lng=&vp_sw_lat=&vp_sw_lng=&view=list"

def parse_datetime(date_string):
   return datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")

def ticket_availability(m_placemark):
    if m_placemark["price_range"] == "Free":
        return True
    else:
        return (m_placemark["ticket_availability"]["remaining_capacity"] > 0)

def null_check(m_placemark, val):
    if val in m_placemark:
        return m_placemark[val]
    else:
        return ""


def parse_events(EVENTS_ENDPOINT):
    response = requests.get(EVENTS_ENDPOINT)
    events = []
    for placemark in response.json()["events"]:
        #if placemark["venue"]["address"]["city"] == "Victoria":
            events.append(
                models.Event(
                    placemark["category"]["name"] if placemark["category"] else "",
                    placemark["name"]["text"],
                    null_check(placemark["venue"],"name") +" ," + placemark["venue"]["address"]["address_1"],
                    placemark["description"]["text"],
                    null_check(placemark["venue"]["address"],"latitude"),
                    null_check(placemark["venue"]["address"],"longitude"),
                    null_check(placemark["venue"]["address"], "postal_code"),
                    placemark["price_range"],
                    ticket_availability(placemark),
                    placemark["start"]["date_header"],
                    parse_datetime(placemark["start"]["local"]),
                    parse_datetime(placemark["end"]["local"]),
                )
            )

    print "Adding {} events to database".format(len(events))
    database.db_session.add_all(events)
    database.db_session.commit()

def run_scraper():
    response = requests.get(TOURISM_VICTORIA_EVENTS_ENDPOINT.format(""))
    page_count = response.json()["pagination"]["page_count"]

    parse_events(TOURISM_VICTORIA_EVENTS_ENDPOINT.format(""))
    if page_count > 1:
        page_number = 2
        while page_number < page_count:
            parse_events(TOURISM_VICTORIA_EVENTS_ENDPOINT.format(page_number))
            page_number+=1


if __name__ == "__main__":
    run_scraper()

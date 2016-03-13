import requests

import database
import models


TOURISM_VICTORIA_EVENTS_ENDPOINT = ""

def main():
    response = requests.get(TOURISM_VICTORIA_EVENTS_ENDPOINT)

    events = []
    for placemark in response.json()["placemarks"]:
        events.append(
            models.Event(
                placemark["venue"],
                placemark["address"],
                placemark["description"],
                placemark["image"],
                placemark["latitude"],
                placemark["longitude"],
                placemark["phone"],
                placemark["subcategory"],
                placemark["website"],
                placemark["zip"],
            )
        )

    print "Adding {} events to database".format(len(events))
    database.db_session.add_all(events)
    database.db_session.commit()


if __name__ == "__main__":
    main()

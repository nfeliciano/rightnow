import requests

import database
import models


TOURISM_VICTORIA_OUTDOOR_ACTIVITIES_ENDPOINT = "http://www.tourismvictoria.com/includes/cfcs/listings/listings_ajax.cfm?menuid=1257&HASDTN=1&MAXSHOW=53&SORTDIR=ASC&SHOWMAP=true&TOTALRESULTS=53&STARTROW=1&SORTBY=dtnRank%20DESC,%20rankid%20ASC,%20sortCompany%20ASC&USERANK=1&SUBCATID=0&DEPARTUREID=0&SFILTER=ALL&CATID=1808&RATES=0&EFILTER=ALL&ITINERARYTHEMEID=0&LISTIDS=0&REGIONID=0&startRow=1"
TOURISM_VICTORIA_NIGHTLIFE_ACTIVITIES_ENDPOINT = "http://www.tourismvictoria.com/includes/cfcs/listings/listings_ajax.cfm?menuid=1585&HASDTN=1&MAXSHOW=20&SORTDIR=ASC&SHOWMAP=false&TOTALRESULTS=20&STARTROW=1&SORTBY=dtnRank%20DESC,%20rankid%20ASC,%20sortCompany%20ASC&USERANK=1&SUBCATID=0&DEPARTUREID=0&SFILTER=ALL&CATID=1818&RATES=0&EFILTER=ALL&ITINERARYTHEMEID=0&LISTIDS=0&REGIONID=0&startRow=1"


def get_activity(ACTIVITY_ENDPOINT):
    response = requests.get(ACTIVITY_ENDPOINT)

    activities = []
    for placemark in response.json()["placemarks"]:
        activities.append(
            models.Activity(
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

    print "Adding {} activities to database".format(len(activities))
    database.db_session.add_all(activities)
    database.db_session.commit()

def run_scraper():

    list_of_activities = []
    list_of_activities.append(TOURISM_VICTORIA_OUTDOOR_ACTIVITIES_ENDPOINT)
    list_of_activities.append(TOURISM_VICTORIA_NIGHTLIFE_ACTIVITIES_ENDPOINT)

    for each_activity in list_of_activities:
        get_activity(each_activity)


if __name__ == "__main__":
    run_scraper()

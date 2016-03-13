import requests


TOURISM_VICTORIA_RESTAURANTS_ENDPOINT = "http://www.tourismvictoria.com/includes/cfcs/listings/listings_ajax.cfm?menuid=1255&HASDTN=1&MAXSHOW=162&SORTDIR=ASC&SHOWMAP=true&TOTALRESULTS=162&STARTROW=1&SORTBY=dtnRank%20DESC,%20rankid%20ASC,%20sortCompany%20ASC&USERANK=1&SUBCATID=0&DEPARTUREID=0&SFILTER=ALL&CATID=1806&RATES=0&EFILTER=ALL&ITINERARYTHEMEID=0&LISTIDS=0&REGIONID=0&startRow=11"


def main():
    response = requests.get(TOURISM_VICTORIA_RESTAURANTS_ENDPOINT)

    for placemark in response.json()["placemarks"]:
        print placemark["venue"]


if __name__ == "__main__":
    main()

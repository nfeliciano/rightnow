from database import init_db
import scrape_restaurants
import scrape_activities
import scrape_events

if __name__ == '__main__':
    init_db()
    scrape_restaurants.run_scraper()
    scrape_activities.run_scraper()
    scrape_events.run_scraper()

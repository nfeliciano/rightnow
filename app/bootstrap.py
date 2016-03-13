from database import init_db
import scrape_restaurants


if __name__ == '__main__':
    init_db()
    scrape_restaurants.run_scraper()

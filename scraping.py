import cloudscraper
from bs4 import BeautifulSoup
import time

scraper = cloudscraper.create_scraper()

BASE_URL = "https://www.albumoftheyear.org/ratings/user-highest-rated/all/"
pages_to_scrape = 10   # NO MORE THAN 40! Scrape atleast with honor
all_album_data = []

for page in range(1, pages_to_scrape + 1):
    url = f"{BASE_URL}{page}/"
    response = scraper.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        albums = soup.find_all('div', class_='albumListRow')

        for album in albums:

            title_artist = album.find('h2', class_='albumListTitle')
            title_artist_text = title_artist.text.strip() if title_artist else "Unknown - Unknown"
            artist,title = title_artist_text.split(' - ', 1) if ' - ' in title_artist_text else ("Unknown", "Unknown")

            album_link = title_artist.find('a')['href'] if title_artist.find('a') else "No link"

            release_date = album.find('div', class_='albumListDate')
            release_date_text = release_date.text.strip() if release_date else "Unknown"

            genres = album.find('div', class_='albumListGenre')
            genres_text = genres.text.strip() if genres else "Unknown"

            score_value = album.find('div', class_='scoreValue')
            score_value_text = score_value.text.strip() if score_value else "0"

            rating_count = album.find('div', class_='scoreText')
            rating_count_text = rating_count.text.strip() if rating_count else "0 ratings"

            all_album_data.append({
                'title': title,
                'artist': artist,
                'release_date': release_date_text,
                'genres': genres_text,
                'user_score': score_value_text,
                'rating_count': rating_count_text,
                'album_link': f"https://www.albumoftheyear.org{album_link}"
            })

        time.sleep(5)

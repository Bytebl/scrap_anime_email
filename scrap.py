import requests
from bs4 import BeautifulSoup

def scrape_top_animes():
    url = "https://myanimelist.net/topanime.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all("h3", class_="fl-l fs14 fw-b anime_ranking_h3")
    result = "🎌 Top 5 Animes do MyAnimeList:\n\n"

    for i, title in enumerate(titles[:5]):
        result += f"{i+1}. {title.get_text(strip=True)}\n"

    return result

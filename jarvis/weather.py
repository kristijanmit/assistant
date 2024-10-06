import requests
from bs4 import BeautifulSoup

def get_weather(city):
    """Scrape weather data for a given city from TimeAndDate."""
    url = f"https://www.timeanddate.com/weather/{city}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Sorry, I couldn't retrieve the weather information."

    soup = BeautifulSoup(response.content, "html.parser")

    temperature = soup.find("div", {"class": "h2"}).text.strip()

    return f"The current temperature in {city} is {temperature}."

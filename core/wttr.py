import httpx


def get_weather(cities: list[str]) -> str:
    results = ""
    for city in cities:
        weather_response = httpx.get(f'https://wttr.in/{city}?T')
        results += weather_response.text
        results += "\n"
    return results

from bs4 import BeautifulSoup
import requests
from unidecode import unidecode


class Text():
    def __init__(self):
        pass

    def bhagavatam(canto, chapter, sloka):

        headers = {'User-Agent': 'Your User Agent String'}

        link = f'https://vedabase.io/en/library/sb/{canto}/{chapter}/{sloka}/'

        try:
            response = requests.get(link, headers=headers, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            return f"Error making HTTP request: {e}"
        except Exception as e:
            return f"Error: {e}"

        vedabase_pg = response.text

        soup = BeautifulSoup(vedabase_pg, "html.parser")

        div_element = soup.find(name="div", class_="wrapper-translation")

        translation = unidecode(div_element.getText())

        return (translation)

import urllib.request
from bs4 import BeautifulSoup

#Получаем исходный код страницы
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

#Парсим секреты с одной страницы в список.
def scraping_secrets(html):
    soup = BeautifulSoup(html)
    secrets = []
    div = soup.find_all('div', class_ = 'shortContent')
    for secret in div:
        secrets.append(secret.text)
    return secrets

#Переходим на следующую страницу.
def paginate (url):
    if ("page" in url):
        cols = url.split('/')
        cols[-1] = str(int(cols[-1]) + 15)
        return "/".join(cols)
    else:
        return url + "/page/15"

#Парсим все секреты из категории в список списков (потому что иногда полезно было бы вытащить секреты с одной страницы, а не со всех разом).
def scraping_all_secrets (url):
    secrets = []
    while (not "В данную категорию пока не добавлено ни одного секрета." in BeautifulSoup(get_html(url)).text):
        secrets.append(scraping_secrets(get_html(url)))
        url = paginate(url)
    return secrets

#Делаем список из списка списков списков (категория-страница-секрет).
def make_beautiful_list (list):
    return [item for sublist in [item for sublist in list for item in sublist] for item in sublist]

def main():
    secrets = []
    vulgar = 'https://ideer.ru/secrets/vulgar'
    angry = 'https://ideer.ru/secrets/angry'
    pizdec = 'https://ideer.ru/secrets/pizdec'
    lust = 'https://ideer.ru/secrets/lust'
    cherhuha = 'https://ideer.ru/secrets/cherhuha'
    cruelty = 'https://ideer.ru/secrets/cruelty'
    ebanko = 'https://ideer.ru/secrets/ebanko'
    fuuu = 'https://ideer.ru/secrets/fuuu'
    betrayal = 'https://ideer.ru/secrets/betrayal'
    alco = 'https://ideer.ru/secrets/alco'
    boom = 'https://ideer.ru/secrets/boom'
    envy = 'https://ideer.ru/secrets/envy'
    enrage = 'https://ideer.ru/secrets/enrage'

    bad_category = [vulgar, angry, pizdec, lust, cherhuha, cruelty, ebanko, fuuu, betrayal, alco, boom, envy, enrage]

    for category in bad_category:
        secrets.append(scraping_all_secrets(category))

    flatten_secrets = (make_beautiful_list(secrets))

    print(flatten_secrets)

if __name__ == '__main__':
    main()

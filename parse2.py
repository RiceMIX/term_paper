import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from parse1 import x, parse


def poiskpers(nick):
    q = format(quote(nick))
    geourl = "https://pogoda33.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-"+q+"/%D0%B4%D0%B5%D0%BD%D1%8C"
    return geourl


tmp_url = poiskpers(x)

URL1 = tmp_url
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/88.0.4324.190 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    items1 = soup.find_all('div', class_='current-weather')

    pog1 = []
    pog2 = []
    pog3 = []
    pog4 = []

    for item in items1:
        pog1.append(dict(
            grad=item.find('div', class_='current-weather-temperature').get_text(),
        ))

    items2 = soup.find_all('div', class_='days d-none d-lg-block')[0]
    into = items2.find_all('div', class_='col-md-1 temperature')

    for i in range(len(into)):
        pog2.append(into[i].text)

    items3 = soup.find_all('div', class_='current-weather-middle-forecast')[0]
    it3 = items3.find_all('div', class_='forecast-weather-temperature')

    items3 = soup.find_all('div', class_='current-weather-middle-forecast')[1]
    it4 = items3.find_all('div', class_='forecast-weather-temperature')

    pog3.append(it3[0].text)
    pog3.append(it4[0].text)

    for i in pog1:
        p1 = i

    items4 = soup.find_all('div', class_='days d-none d-lg-block')[0]
    into4 = items4.find_all('div', class_='col-md-1 time')

    for i in range(len(into4)):
        pog4.append(into4[i].text)

    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("Джерело №2")
    print("\t\t\t\t\t\t\t\t\t\tПогода "+x)
    print("Температура прямо  зараз: "+p1['grad'])
    print("Температура: вдень "+pog3[0], "||", "\tввечері "+pog3[1])
    print("Прогноз на день")
    for i in pog4:
        print(i[:-2]+":00", end='       ')
    print()
    for i in pog2:
        print(i, end='       ')
        if i == pog2[4]:
            print(end='  ')
        if i == pog2[5]:
            print(end=' ')

    print()
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


def parse():
    html = get_html(URL1)
    print(html)

    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error")


parse()
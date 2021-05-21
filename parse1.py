import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def poiskpers(nick):
    geourl = "https://ua.sinoptik.ua/{0}".format(quote(nick))
    return geourl


x = str(input("Enter:"))


tmp_url = poiskpers("погода-"+x)

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

    items = soup.find_all('div', class_='main loaded')

    weather1 = []
    weather2 = []
    weather3 = []

    for item in items:
        weather1.append(dict(
            title=item.find('p', class_='day-link').get_text(),
            date1=item.find('p', class_='date').get_text(),
            date2=item.find('p', class_='month').get_text(),
            temp=item.find('div', class_='min').get_text(),
            temp2=item.find('div', class_='max').get_text()))

    item2 = soup.find_all('div', class_='tabsContentInner')

    for item in item2:
        weather2.append(dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                             vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                             vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                             vol7=item.find('td', class_='p7').get_text(),
                             vol8=item.find('td', class_='p8').get_text()))

    item3 = soup.find_all('tr', class_='temperature')

    for item in item3:
        weather3.append(dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                             vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                             vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                             vol7=item.find('td', class_='p7').get_text(),
                             vol8=item.find('td', class_='p8').get_text()))

    for i in weather1:
        w1 = i
    for i in weather2:
        w2 = i
    for i in weather3:
        w3 = i
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("Джерело №1")
    print("\t\t\t\t\t\t\t\t\t\tПогода "+x)
    print("День:"+w1['title'])
    print("Число: "+w1['date1'], ' ', w1['date2'])
    print("Температура: :"+w1['temp'], " ||  "+w1['temp2'])
    print()

    mw2 = []
    for i in w2:
        mw2.append(w2[i])
    mw3 = []
    for i in w3:
        mw3.append(w3[i])
    print("Прогноз на день")
    for i in mw2:
        print(i, end='     ')
    print()
    for j in mw3:
        print(j, end='       ')
        if j == mw3[4]:
            print(end='  ')
        if j == mw3[5]:
            print(end='  ')

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

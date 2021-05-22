from oop_parse import get_html
from bs4 import BeautifulSoup

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
    print("\t\t\t\t\t\t\t\t\t\tПогода ")
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

def par():
    Obj1 = get_html("Дубляни")
    s_sinoptik = Obj1.poiskpres_sinoptik()

    html_sinoptik = Obj1.g_html_sinoptik(s_sinoptik)
    print(html_sinoptik)
    html_pogoda = Obj1.g_html_sinoptik(s_sinoptik)
    print(html_pogoda)
    if html_pogoda.status_code == 200:
        get_content(html_pogoda.text)
    else:
        print("\nError")
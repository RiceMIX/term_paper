import requests
from bs4 import BeautifulSoup
from urllib.parse import quote



class link:
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
        'Chrome/88.0.4324.190 Safari/537.36',
        'accept': '*/*'}

    def __init__(self, name):
        self.name = name
        self.q = format(quote("погода-"+self.name))

    def poiskpres_sinoptik(self):
        self.url_s = "https://ua.sinoptik.ua/{0}".format(self.q)
        return self.url_s

    def poiskpres_pogoda(self):
        self.url_p = "https://pogoda33.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-" + self.q + "/%D0%B4%D0%B5%D0%BD%D1%8C"
        return self.url_p




class get_html(link):
    def g_html_sinoptik(self, url, params=None):
        self.url = url
        self.r_s = requests.get(self.url, headers=self.HEADERS, params=params)
        return self.r_s

    def g_html_pogoda(self, url, params=None):
        self.url = url
        self.r_p = requests.get(self.url, headers=self.HEADERS, params=params)
        return self.r_p








class get_content_sin:
    def __init__(self, name):
        self.html = name
        self.soup = BeautifulSoup(self.html, 'html.parser')

        self.items = self.soup.find_all('div', class_='main loaded')
        self.item2 = self.soup.find_all('div', class_='tabsContentInner')
        self.item3 = self.soup.find_all('tr', class_='temperature')

        self.weather1 = []
        self.weather2 = []
        self.weather3 = []

    def find_elem(self):
        for i in self.items:
            self.weather1.append(dict(
                title=i.find('p', class_='day-link').get_text(),
                date1=i.find('p', class_='date').get_text(),
                date2=i.find('p', class_='month').get_text(),
                temp=i.find('div', class_='min').get_text(),
                temp2=i.find('div', class_='max').get_text()))

        for item in self.item2:
            self.weather2.append(
                dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                     vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                     vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                     vol7=item.find('td', class_='p7').get_text(),
                     vol8=item.find('td', class_='p8').get_text()))

        for item in self.item3:
            self.weather3.append(
                dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                     vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                     vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                     vol7=item.find('td', class_='p7').get_text(),
                     vol8=item.find('td', class_='p8').get_text()))

        for i in self.weather1:
            self.w1 = i
        for i in self.weather2:
            self.w2 = i
        for i in self.weather3:
            self.w3 = i


class show_content_sin(get_content_sin):
    def __init__(self, name):
        super().__init__(name)
        self.mw3 = []
        self.mw2 = []

    def show(self):

        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Джерело №1")
        print("\t\t\t\t\t\t\t\t\t\tПогода ")
        print("День:" + self.w1['title'])
        print("Число: " + self.w1['date1'], ' ', self.w1['date2'])
        print("Температура: :" + self.w1['temp'], " ||  " + self.w1['temp2'])
        print()

        for i in self.w2:
            self.mw2.append(self.w2[i])
        for i in self.w3:
            self.mw3.append(self.w3[i])
        print("Прогноз на день")
        for i in self.mw2:
            print(i, end='     ')
        print()
        for j in self.mw3:
            print(j, end='       ')
            if j == self.mw3[4]:
                print(end='  ')
            if j == self.mw3[5]:
                print(end='  ')

        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

class get_content_pog:
    def __init__(self, name):

        self.soup = BeautifulSoup(name, 'html.parser')


        self.pog1 = []
        self.pog2 = []
        self.pog3 = []
        self.pog4 = []





        self.items2 = self.soup.find_all('div', class_='days d-none d-lg-block')[0]
        self.into = self.items2.find_all('div', class_='col-md-1 temperature')



        self.items3 = self.soup.find_all('div', class_='current-weather-middle-forecast')[0]
        self.it3 = self.items3.find_all('div', class_='forecast-weather-temperature')

        self.items3 = self.soup.find_all('div', class_='current-weather-middle-forecast')[1]
        self.it4 = self.items3.find_all('div', class_='forecast-weather-temperature')


        self.pog3.append(self.it3[0].text)
        self.pog3.append(self.it4[0].text)



        self.items4 = self.soup.find_all('div', class_='days d-none d-lg-block')[0]
        self.into4 = self.items4.find_all('div', class_='col-md-1 time')

    def find_elem(self):

        for i in range(len(self.into)):
            self.pog2.append(self.into[i].text)

        self.items1 = self.soup.find_all('div', class_='current-weather')
        for item in self.items1:
            self.pog1.append(dict(
                grad=item.find('div', class_='current-weather-temperature').get_text(),
            ))

        for i in self.pog1:
            self.p1 = i

        for i in range(len(self.into4)):
            self.pog4.append(self.into4[i].text)






class show_content_pog(get_content_pog):

    def show(self):

        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Джерело №2")
        print("\t\t\t\t\t\t\t\t\t\tПогода ")
        print("Температура прямо  зараз: " + self.p1['grad'])
        print("Температура: вдень " + self.pog3[0], "||", "\tввечері " + self.pog3[1])
        print("Прогноз на день")
        for i in self.pog4:
            print(i[:-2] + ":00", end='       ')
        print()
        for i in self.pog2:
            print(i, end='     ')
            if i == self.pog2[4]:
                print(end='  ')
            if i == self.pog2[5]:
                print(end=' ')

        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")



def parse():
    x = str(input("Enter:"))

    Obj1 = get_html(x)
    s_sinoptik = Obj1.poiskpres_sinoptik()
    s_pogoda= Obj1.poiskpres_pogoda()


    html_sinoptik = Obj1.g_html_sinoptik(s_sinoptik)
    print(html_sinoptik)
    html_pogoda = Obj1.g_html_pogoda(s_pogoda)
    print(html_pogoda)

    if html_sinoptik.status_code == 200:
        Obj2 = show_content_sin(html_sinoptik.text)
        Obj2.find_elem()
        Obj2.show()
    if html_pogoda.status_code == 200:
        Obj3 = show_content_pog(html_pogoda.text)
        Obj3.find_elem()
        Obj3.show()
    else:
        print("\nError")



parse()







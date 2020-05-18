import requests
from bs4 import BeautifulSoup

class Parse_weather():
    def get_data(self):
        result = requests.get('https://yandex.ru/pogoda/saint-petersburg')
        self.soup = BeautifulSoup(result.text, 'html.parser')
        div = self.soup.findAll('div')
        soup = self.soup
        div = soup.find( 'div', {'class': 'content__row'} )
        place = div.find( 'h1', {'class': True} )
        temp = div.find( 'span', {'class': 'temp__value'} )
        status = div.find( 'div', {'class': 'link__condition day-anchor i-bem'} )
        feeling = div.find( 'div', {'class': 'term term_orient_h fact__feels-like'} ). \
            find( 'span', {'class': 'temp__value'} )
        wind_speed = div.find( 'span', {'class': 'wind-speed'} )
        wind_way = div.find( 'abbr', {'class': 'icon-abbr'} )
        humidity = div.find( 'div', {'class': 'term term_orient_v fact__humidity'} ). \
            find( 'div', {'class': 'term__value'} )

        pressure = div.find( 'div', {'class': 'term term_orient_v fact__pressure'} ). \
            find( 'div', {'class': 'term__value'} )

        reply = place.text + '\n' + \
                'Температура:' + temp.text + '°C' + '\n' + \
                'На улице:' + status.text + '\n' + \
                'Ощущается как: ' + feeling.text + '°C' + '\n' + \
                'Ветер: ' + wind_speed.text + ' м/с ' + wind_way.text + '\n' + \
                'Влажность: ' + humidity.text + '\n' + \
                'Давление: ' + pressure.text + '\n'
        return reply

answer = Parse_weather()
weather = answer.get_data()

print(weather)
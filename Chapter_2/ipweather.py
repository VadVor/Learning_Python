from requests import get

ip = '178.168.207.5'

latlong = get('https://ipapi.co/{}/latlong/'.format(ip)).text.split(',')

weather = get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=2aa31e18326228407c8495bea9ad311b&units'
'=metric&lang=ru'.format(latlong[0],latlong[1])).json()
print(weather ['name'],weather ['main']['temp'],'C')

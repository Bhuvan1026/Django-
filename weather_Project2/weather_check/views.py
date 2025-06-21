from django.shortcuts import render
import requests

# Replace this with your actual API key from OpenWeatherMap
API_KEY = '15bec62b728d82eecf4b5f2ede85ad6b'

def index(request):
    country_code = coordinate = temp = pressure = humidity = None

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                country_code = data['sys']['country']
                coordinate = f"Latitude: {data['coord']['lat']}, Longitude: {data['coord']['lon']}"
                temp = f"{data['main']['temp']} °C"
                pressure = f"{data['main']['pressure']} hPa"
                humidity = f"{data['main']['humidity']}%"
            else:
                # Optional: Handle invalid city error
                country_code = coordinate = temp = pressure = humidity = None

    return render(request, 'index.html', {
        'country_code': country_code,
        'coordinate': coordinate,
        'temp': temp,
        'pressure': pressure,
        'humidity': humidity,
    })

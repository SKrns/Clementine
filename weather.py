import pyowm
owm = pyowm.OWM('44d2cfac92a84e3b2852153c8aeb3384')
#location=input()
location='seoul'
location+=',kr'
observation = owm.weather_at_place(location)
w = observation.get_weather()
wind = w.get_wind()
temperature=w.get_temperature('celsius')
tomorrow=pyowm.timeutils.tomorrow()
wind = w.get_wind()

print(w)
print(wind)
print(temperature)
print(tomorrow)

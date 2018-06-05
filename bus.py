
#from urllib2 import Request, urlopen
import urllib.request
import requests
import urllib.parse
#from urllib import urlencode, quote_plus


url = 'http://openapi.gbis.go.kr/ws/rest/busarrivalservice'
queryParams = '?' + urllib.parse.urlencode({ quote('ServiceKey') : 'NlQF4lQIqhWlOsoW1jeJi7J5qsQs82SdJ0BKP69b8VnhM9ga6AccQgs9TjsO%2BFB5%2FMvi0BM1mi1e8vl%2FjMmrvQ%3D%3D', quote('stationId') : '200000078', quote('routeId') : '233000031', quote('staOrder') : '17' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print (response_body)

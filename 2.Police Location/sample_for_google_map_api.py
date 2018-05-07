import googlemaps
from datetime import datetime

# Google Map Python API : https://github.com/googlemaps/google-maps-services-python
gmaps = googlemaps.Client(key='AIzaSyBzUAmLg4Q5l9G4DH7LnllAh7X-VtHNGc8')

# Geocoding an address
google_address = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
google_in_eng = gmaps.geocode('Google')
# https://www.google.com/maps/place/%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%EC%B2%AD/@37.5638165,126.9751701,15z/data=!4m8!1m2!2m1!1z7ISc7Jq4IOyLnOyyrQ!3m4!1s0x0:0xe92b70ac420cf0a8!8m2!3d37.5662959!4d126.9779447
seoul_city_hall = gmaps.geocode('서울시청', language='ko')

# Look up an address with reverse geocoding
google_reverse_geocode = gmaps.reverse_geocode((40.714224, -73.961452))
seoul_city_hall_reverse_geocode = gmaps.reverse_geocode((37.5638165, 126.9751701), language='ko')

# Request directions via public
# 별도의 인증 필요
#  - https://console.developers.google.com/
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
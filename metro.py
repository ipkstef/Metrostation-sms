import schedule 
import time
import requests 
import json

API_KEY = '1eef91543ea14395b36b1494aa65dce6'
REQUEST_URL = 'https://api.wmata.com/StationPrediction.svc/json/GetPrediction/all'

CRYSTAL_CITY_CODE = 'C09'
FRANCONIA_CODE = 'J03'

def connection_object(stationcode,origin):
	url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{}".format(stationcode)

	headers = {
	    "api_key": "1eef91543ea14395b36b1494aa65dce6"    
	}

	response = requests.get(url, headers=headers) 
	hello = response.json()


	for station in hello["Trains"]:
		print("These trains are on the way to "+ origin +"! \n" "Destination Name: " +station["DestinationName"], "\n" "Arrival Min: "+station["Min"], "\n" "Line Color: " + station["Line"], "\n" "--------")

















# schedule.every(5).seconds.do(work)
schedule.every(4).seconds.do(connection_object, stationcode=FRANCONIA_CODE, origin='Work')




while True:
	schedule.run_pending()
	time.sleep(1)
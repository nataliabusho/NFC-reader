import requests
import json


domainName = 'https://attendance-server-gr.herokuapp.com'

def findLocationbyID(locationID) :
    url = domainName + '/location'
    response = requests.get(url, params = {'id' : locationID})
    if response.status_code !=200:
        print('Invaliid location id Given. That location does not exist')
        exit()
    location = json.loads(response.text)
    print('------  ' + location['name'] + ' ----')

def saveAppearance(locationID, rfID) :
    url = domainName + '/appearance/create'
    payload = {'locationID': locationID, 'rfID': rfID}
    response = requests.post(url, json = payload)
    if response.status_code !=200:
        print('User appearance couldnt be recorded')
        return False
    print('apperance recorded')
    return True

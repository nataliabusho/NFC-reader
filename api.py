import requests
import json


domainName = 'https://attendance-server-gr.herokuapp.com'

def findUserByRFID(RFID) :
    url = domainName + '/users'
    response = requests.get(url, params = {'id' : RFID})
    user = json.loads(response.text)
    print('welcome ' + user['name'] + ' ' + user['lastName'])
    return user

def saveAppearance(userID, locationID) :
    url = domainName + '/appearance/create'
    payload = {'userID': userID, 'locationID': locationID}
    print(payload)
    response = requests.post(url, json = payload)
    print(response)
    print('apperance recorded')

import pytest
import requests

### Parameters ###
api_login = 'global'
api_pass = 'global'
base_url = 'http://10.94.6.100:50000'

@pytest.fixture(scope="function", autouse=True)
def setup():
    global cookies
    print("Getting token...")
    data_get = {'UserName' : api_login, 'Password' : api_pass, 'RememberMe' : False}
    #headers = {'disabled': 'false', 'description': {'content': 'Referer', 'type': 'text/plain'}, 'key': 'Referer', 'name': 'Referer', 'value': '{base_url} + "/Home/Homepage"'}
    response = requests.post(base_url + '/login', data=data_get)
    if response.ok:
        cookies = dict(response.cookies)
        print("Cookies: ", cookies)
        return cookies
    else:
        print("HTTP %i - %s, Message %s" % (response.status_code, response.reason, response.text))

def test_user_creates_teams(setup):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Connection': 'keep-alive'}
    data_get = {'artists':[],
        'shotTeamName': 'KateTestingAPIByPython',
        'color':'#FFFFFF',
        'departmentId':'',
        'showID':'null',
        'siteID':'',
        'dates':{
        'start':'2022-04-11T10:47:25.523Z', 
        'end': ''
        },
        'end':'',
        'start':'2022-04-11T10:47:25.523Z'}
    response = requests.post(base_url + '/api/ShotTeamsNewApi/CreateShotTeam/', data=data_get, cookies=cookies, headers=headers)
    print (response.text)
    assert response.status_code == 200
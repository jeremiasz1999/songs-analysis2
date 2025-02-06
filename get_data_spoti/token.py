import base64
import requests

CLIENT_ID = 'd35fd359ca1c4d209f81e7abbb6c8940'
CLIENT_SECRET = '241efb6072dd4878a942a8c197fbe343'

# Funkcja uzyskania tokenu
def get_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=data)
    return response.json()

# Wyświetla token
token_response = get_token()
print(token_response)
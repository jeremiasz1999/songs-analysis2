import requests

# Token dostępu
TOKEN = 'BQcxANkkWuwvW3p8qZV0LRMiFimjWDDSLSJZOm7t7YvHbLGN1UgZmPMSb_uZH6glltTkMO5IRhxdLsvJUOHo-MtYGqa8BJFSyFI8'

# ID utworu
TRACK_ID = "3n3Ppam7vgaVa1iaRUc9Lp"

# Wysyłanie żądania
url = f"https://api.spotify.com/v1/audio-features/{TRACK_ID}"
headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.get(url, headers=headers)

# Obsługa odpowiedzi
if response.status_code == 200:
    print("Sukces:", response.json())
elif response.status_code == 403:
    print("Błąd 403: Brak uprawnień lub problem z tokenem.")
    print(response.json())
else:
    print(f"Błąd {response.status_code}: {response.text}")
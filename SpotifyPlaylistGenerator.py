import requests
import json

endpoint_url = "https://api.spotify.com/v1/recommendations?"
access_token = 'BQD8xJ3wywk6QKmIAo8osrywPDVVa1aQrWrfPrzYsB2x3MDQaLIUoUGMObJSDVy9jCHGuM_17BbBgqKhgmR2-gyswdOI32kE7LDv_4O47kQ9LmORNIyFAssvzq7voRz-Jqs6Ij4ZXOqeVFHxfsJC6PrmLJnrSOnBrKuMltQAwTIaxvBvrtQjKoG7AYjfGH-AbVC8lvc8fYzdpVHDzTK7YWtqKFy3'
uris = []



#FILTERS
limit = 10 #number of songs in playlist
market = "AU"
seed_genres = "dance"
target_danceability = 0.8
valence = '0.1'
seed_artists = "5cj0lLjcoR7YOSnhnX0Po5,1Xyo4u8uXC1ZmMpatF05PJ"

query = f'{endpoint_url}limit={limit}&market={market}&seed_artists={seed_artists}&valence={valence}&target_danceability={target_danceability}'

response =requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

json_response = response.json() #JSON data of songs

for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

'''
Session 2 - Creating a playlist in Spotify! 
'''

#CREATE EMPTY PLAYLIST
user_id = "ENTER YOUR USERNAME or URI" #this is the username you log in with
endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "PYTHON DANCE PLAYLIST",
          "description": "I made this with Python!!",
          "public": False # let's keep it between us - for now
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", "Authorization":"Bearer " + access_token})
print(response.status_code)

#PUT SONGS IN PLAYLIST
playlist_id = response.json()['id']
endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", "Authorization":f"Bearer {access_token}"})
print(response.status_code)



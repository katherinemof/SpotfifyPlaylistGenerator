import requests
import json
#URLS
endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = ''
limitsong = 2 #NOTE: limitsong and limitartist must be less than 5 in TOTAL
limitartist = 3
personal_artist_url = f'https://api.spotify.com/v1/me/top/artists?limit={limitartist}'
personal_track_url = f'https://api.spotify.com/v1/me/top/tracks?limit={limitsong}'

#Personalisation
artists = '' #string that will be used in the filters for seed_artist
response =requests.get(personal_artist_url,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})
print(response)
count = 0
for i in response.json().get("items"):
    artists+=(str(i.get("id")))
    if(count != limitartist-1):
        artists+= ','
        count+=1
print(artists)

#get songs
songs = ''
response =requests.get(personal_track_url,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})
print(response)
count = 0

for i in response.json().get("items"):
    print(i)
    songs += (str(i.get("id")))
    if(count != limitsong-1):
        songs+= ','
        count+=1
print(songs)



#FILTERS
limit = 10 #number of songs in playlist
market = "AU"
seed_genres = "dance"
target_danceability = 0.8
valence = '0.1'
seed_artists = artists
seed_tracks = songs
uris = []
query = f'{endpoint_url}limit={limit}&market={market}&seed_artists={seed_artists}&valence={valence}&target_danceability={target_danceability}&seed_tracks={seed_tracks}'

response =requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

print(response)
json_response = response.json()
print(json_response)

for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

# CREATE A NEW PLAYLIST
user_id = "ENTER SPOTIFY USERNAME"
endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "Based off top songs and artists",
          "description": "Based off your music",
          "public": False
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json",
                       "Authorization":f"Bearer {access_token}"})


print(response.json())

#ADD SONGS TO PLAYLIST
playlist_id = response.json()['id']
endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

print(response.status_code)
import requests
import json
#URLS
endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = ''
personal_artist_url = 'https://api.spotify.com/v1/me/top/artists?limit=3'
limit = 5
personal_track_url = f'https://api.spotify.com/v1/me/top/tracks?limit={limit}'


#Personalisation
artists = ''
response =requests.get(personal_artist_url,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})
print(response)
count = 0
for i in response.json().get("items"):
    print(i)
    artists+=(str(i.get("id")))
    if(count != limit-1):
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
    if(count != limit-1):
        songs+= ','
        count+=1
print(songs)



#FILTERS
limit = 15 #number of songs
market = "AU"
seed_genres = "pop"
target_danceability = 1
seed_artists = artists
seed_tracks = songs
seed_tracks = ''
valence = '0.1'
uris = []
target_energy='0.9'

#QUERY FOR SONGS
query = f'{endpoint_url}limit={limit}&market={market}&seed_artists={seed_artists}&target_danceability={target_danceability}&seed_tracks={seed_tracks}&valence={valence}&target_energy={target_energy}'


response =requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

print(response)
json_response = response.json()

for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

# CREATE A NEW PLAYLIST
user_id = "katherinemof"
endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "SUPER UPBEAT",
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
#response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json",
#                        "Authorization":f"Bearer {access_token}"})

#print(response.status_code)
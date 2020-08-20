import requests
import json

endpoint_url = "https://api.spotify.com/v1/recommendations?"
access_token = "BQD1zZTreOMg4bz9Fdq9Csd1V8MczzULXG3Idr5kMSICmjCNNUprJKIiqH7v7Af0lreOqPcwB6h1eEXdrccAUxjc5gvnJ9aXrhvcgPMmSZbBBPp6fkbLzRMSTlHMRNwBGWj1VZpMfQNpRCw7V5naJoJ3GxNWzgKWj-DhKvfR1dPJoRCRyvh0gaiuOnDk2Gw9Zft3PEcZm78mImmiNPws-i4EB7Fm"
uris = []



#FILTERS
limit = 10 #number of songs in playlist
market = "AU"
seed_genres = "dance"
target_danceability = 0.8
seed_artists = "06HL4z0CvFAxyc27GXpf02"

query = f'{endpoint_url}limit={limit}&market={market}&seed_artists={seed_artists}&target_danceability={target_danceability}'

response =requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

json_response = response.json() #JSON data of songs

for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")


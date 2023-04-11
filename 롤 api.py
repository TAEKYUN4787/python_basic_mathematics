import requests

# Replace <api_key> with your Riot Games API key
api_key = "<api_key>"
summoner_name = "example_summoner_name"

# Define the API endpoint for retrieving summoner information
endpoint = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}"

# Send a GET request to the API endpoint
response = requests.get(endpoint)

# Check the status code of the response to ensure it was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    # Access the information about the summoner
    summoner_id = data["id"]
    summoner_name = data["name"]
    summoner_level = data["summonerLevel"]
    print(f"Summoner ID: {summoner_id}")
    print(f"Summoner Name: {summoner_name}")
    print(f"Summoner Level: {summoner_level}")
else:
    # If the API request was not successful, raise an error
    response.raise_for_status()

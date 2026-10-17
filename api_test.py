import requests
import json
def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        json_data = response.json()
        return json_data

    except requests.exceptions.RequestException as e:
        print(f"API request failed:{e}")
        return None
    
url = "https://jsonplaceholder.typicode.com/todos/1"



data = fetch_data(url)

if data is not None:
    print("Title:", data["title"])
    print("Complete:",data["completed"])



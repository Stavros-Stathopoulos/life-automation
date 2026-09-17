import os
import time
import requests
from dotenv import load_dotenv
'''
Example:
https://baseUrl/:year/:month/:day

curl --request GET \
	--url https://greek-eortologio.p.rapidapi.com/2026/9/18 \
	--header 'x-rapidapi-host: greek-eortologio.p.rapidapi.com' \
	--header 'x-rapidapi-key: ' + os.getenv("API_KEY")
'''
load_dotenv()
URL = "https://greek-eortologio.p.rapidapi.com/"

def get_nameday(
        day: int,
        month: int,
        year: int
):
    try:
        resp = requests.get(
            URL+f"{year}/{month}/{day}",
            
            headers={
                "x-rapidapi-host": str(os.getenv("API_HOST")),
                "x-rapidapi-key": str(os.getenv("API_KEY"))
            }
        )
    except Exception as e:
        print(f"An error occurred while fetching nameday information: {e}")
        return None

    if resp.status_code == 200:
        return resp.json()
    else:
        return None

if __name__ == "__main__":
    day = time.localtime().tm_mday
    month = time.localtime().tm_mon
    year = time.localtime().tm_year

    try:
        nameday_info = get_nameday(day, month, year)
    except Exception as e:
        print(f"An error occurred while fetching nameday information: {e}")
        nameday_info = None

    if nameday_info:
        print(f"Nameday information for {day}/{month}/{year}:")
        print(nameday_info)
    else:
        print("Failed to retrieve nameday information.")
#import the actual scraper
import requests

url = "http://ip-api.com/json/"
key = requests.get(url)
print(key.text)
if "Croatia" in key.text or "New Zealand" in key.text or "Argentina" in key.text:
    print("Your VPN might not be on !!")
    safe = False
else:
    safe = True

if safe == True:
    import ahmiascraper
    ahmiascraper.Scraper()
else:
    print("IP change failed, try again later.")

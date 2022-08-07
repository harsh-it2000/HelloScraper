 import requests

 url = "http://ip-api.com/json/"
 key = requests.get(url)
 #print(key.text)

 if "India" in key.text or "Mumbai" in key.text or "Delhi" in key.text:
    print ("Your VPN might not be activated")
    safe = False

 else
    safe = True

 if safe == True
    import ahmiascraper
    ahmiascraper.Scraper()
 else
    print("IP Change Failed, Try Again Later.")


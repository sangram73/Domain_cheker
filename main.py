import requests

domain = input("check domain name: ")
response = requests.get(
    url=f"https://api.whoisfreaks.com/v1.0/whois?apiKey=65a7b9e7b5204eff8ca880e216cdc2b4&whois=live&domainName={domain}")
res = response.json()
status = res["domain_registered"]

if status == "yes":
    msg = "Sorry Domain can already tacken"
else:
    msg = "Hurry it's avlevel !"

print(msg)


# import requests

# url = "https://domaination.p.rapidapi.com/domains/%7Bdomain-name%7D"

# headers = {
# 	"X-RapidAPI-Key": "d017b73df2mshd58e554d8099989p16e2c7jsn12371d46cc0f",
# 	"X-RapidAPI-Host": "domaination.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

import requests
from tkinter import *



window=Tk()
window.title("Domain checker")
window.config(padx=20,pady=20)
canvas=Canvas(window,width=500,height=500)
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



import requests
from tkinter import *


window = Tk()
window.title("Domain checker")
window.config(padx=20, pady=20)
window.minsize(width=300, height=300)


def Entry_domain():
    domain = str(input_domain.get())
    response = requests.get(
        url=f"https://api.whoisfreaks.com/v1.0/whois?apiKey=65a7b9e7b5204eff8ca880e216cdc2b4&whois=live&domainName={domain}")
    res = response.json()
    status = res["domain_registered"]


input_domain = Entry(width=10)
input_domain.grid(column=1, row=2)

window.mainloop()

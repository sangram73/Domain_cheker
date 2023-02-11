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


# lable for text show 
label1 = Label(text="Useing Tkinter", font=("Arial",30,"bold"))
label1.grid(column=2, row=0)

# lable for text show 
label2 = Label(text="Domain Name", font=("Sans Serif",22,"bold"))
label2.grid(column=2, row=4)
# entry for get input for user
input_domain = Entry(width=50)
input_domain.grid(column=2, row=5)
# for placeholder the text
input_domain.insert(0, "eg. web-angle.com")


window.mainloop()

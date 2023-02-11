import requests
from tkinter import *


window = Tk()
window.title("Domain checker")
window.config(padx=20, pady=20, background="#4d76a3")
window.minsize(width=300, height=300)


def Entry_domain():
    domain = str(input_domain.get())
    response = requests.get(
        url=f"https://api.whoisfreaks.com/v1.0/whois?apiKey=65a7b9e7b5204eff8ca880e216cdc2b4&whois=live&domainName={domain}")
    res = response.json()
    status = res["domain_registered"]
    input_domain.delete(0, END)

    if status == "yes":
        result = "!ohoo it will be already taken"
        label3.config(background="red")
    else:
        result = "Huryy its available"
        label3.config(background="green")

    label3.config(text=result)


# lable for text show
label1 = Label(text="Useing Tkinter", font=("Arial", 30, "bold"))
label1.grid(column=2, row=0)

# lable for text show
label2 = Label(text="Domain Name", font=("Sans Serif", 22, "bold"))
label2.grid(column=2, row=4,padx=20,pady=20)
# entry for get input for user
input_domain = Entry(width=20,font=("Sans Serif",11))
input_domain.grid(column=2, row=5, padx=30,pady=20)

#  add a submit Button
check = Button(text="Check", background="lightgreen", width=20,
               borderwidth=3, font=("Sans Serif", 10, "bold"), command=Entry_domain)
check.grid(column=2, row=7)
# lable for  show  result
label3 = Label(text="", font=("Sans Serif", 22, "bold"))
label3.grid(column=2, row=9, padx=20, pady=20)


# for placeholder the text
input_domain.insert(0, "eg. web-angle.com")


window.mainloop()

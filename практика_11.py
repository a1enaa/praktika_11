import json
import requests
from tkinter import *

window=Tk()
window.title('Добро пожаловать в приложение')
window.geometry('600x400')

def file(practics,text):
    practics=open('практическая_11','w')
    practics.write(text)




def click():

    try:
        json = requests.get(f"https://api.github.com/users/{pole_vvoda}").json()
    except:
        json = requests.get(f"https://api.github.com/users/wp-calypso").json()
    try:
        company = json["company"]
    except:
        company = None
    try:
        id=json["id"]
    except:
        id=None
    try:
        email=json["email"]
    except:
        email=None
    try:
        name=json["name"]
    except:
        name=None
    try:
        url=json["url"]
    except:
        url=None
    try:
        created_at=json["created_at"]
    except:
        created_at=None
    file('практическая_11',f"'company': {company}\n'created_at': {created_at}\n'email':{email}\n'id':{id}\n'name':{name}\n'url':{url}")
    



button=Button(window,text='нажать', command = click)
button.grid(column=3,row=1)

pole_vvoda=Entry(window,width=8)
pole_vvoda.insert(INSERT,'wp-calypso')
pole_vvoda.grid(column=3,row=0)


window.mainloop()

import json
import os
from customtkinter import *

PATH = os.path.abspath(path = __file__  + "/..")

app = CTk()
app.geometry("500x500")
app.title("json saver")

name_input = CTkEntry(master = app, width = 250, height = 50, placeholder_text= "Enter the name")
name_input.pack()

surname_input = CTkEntry(master = app, width = 250, height = 50, placeholder_text= "Enter the surname")
surname_input.pack()

age_input = CTkEntry(master = app, width = 250, height = 50, placeholder_text= "Enter the age")
age_input.pack()

def save_button_command():
    with open(file = os.path.join(PATH, "json/person.json"), mode = "w") as json_file:
        content = json.loads(s ="{"+f'"name": "{name_input.get()}","surname": "{surname_input.get()}","age": "{age_input.get()}"'+"}")
        json.dump(content, json_file)
        #json_file = json.loads(s =f'"name": "{name_input}","surname": "{surname_input}","age": "{age_input}" ')

save_button = CTkButton(master = app, width = 250, height = 50, text = "Save", command = save_button_command)
save_button.pack()

app.mainloop()
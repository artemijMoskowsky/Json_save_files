import json
import os
from customtkinter import *
from PIL import Image,ImageTk
PATH = os.path.abspath(path = __file__  + "/..")

app = CTk()
app.geometry("448x515")
app.title("json saver")
#app.configure(fg_color = "#4F4F4F")
canvas = CTkCanvas(master = app, width = 448, height = 515)
background = ImageTk.PhotoImage(Image.open(os.path.join(PATH, "images/background.png")))
canvas.pack()
canvas.create_image(224, 257, image = background)

cj_background = ImageTk.PhotoImage(Image.open(os.path.join(PATH, "images/cjbackground.png")))
cj = CTkLabel(master = app, width = 206, height = 45, text = "", image = cj_background)
cj.pack()
cj.place(x = 119, y = 17)


name_input = CTkEntry(master = app, width = 307, height = 66, placeholder_text= "Enter the name", text_color = ("#FFFFFF","#FFFFFF"),placeholder_text_color= "#FFFFFF")
name_input.pack()
name_input.place(x = 72, y = 115)
name_input.configure(fg_color = "#4F4F4F",border_color = "#FCA625", corner_radius = 20, bg_color = "#1B1B1B")

surname_input = CTkEntry(master = app, width = 307, height = 66, placeholder_text= "Enter the surname", text_color = ("#FFFFFF","#FFFFFF"),placeholder_text_color= "#FFFFFF")
surname_input.pack()
surname_input.place(x = 72, y = 226)
surname_input.configure(fg_color = "#4F4F4F",border_color = "#FCA625", corner_radius = 20, bg_color = "#1B1B1B")

age_input = CTkEntry(master = app, width = 307, height = 66, placeholder_text= "Enter the age", text_color = ("#FFFFFF","#FFFFFF"),placeholder_text_color= "#FFFFFF")
age_input.pack()
age_input.place(x = 72, y = 337)
age_input.configure(fg_color = "#4F4F4F",border_color = "#FCA625", corner_radius = 20, bg_color = "#1B1B1B")

def save_button_command():
    with open(file = os.path.join(PATH, "json/person.json"), mode = "w") as json_file:
        content = json.loads(s ="{"+f'"name": "{name_input.get()}","surname": "{surname_input.get()}","age": "{age_input.get()}"'+"}")
        json.dump(content, json_file)


save_button = CTkButton(master = app, width = 114, height = 47, text = "Save", command = save_button_command, font = (None, 19, "bold"))
save_button.pack()
save_button.place(x = 160, y = 459)
save_button.configure(fg_color = "#4F4F4F",border_color = "#FCA625", corner_radius = 20, border_width = 2, bg_color = "#403A3A")

app.mainloop()
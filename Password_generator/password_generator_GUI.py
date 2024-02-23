import tkinter
from tkinter import *
import customtkinter
from customtkinter import *
import random
import string 


def sliding(value):
    label_slider.configure(text=int(value))

def generate_password():
    length = int(slider.get())
    custom_characters = '!#$%&/=*+@-~?'
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + custom_characters
    password = ''.join(random.choice(characters) for _ in range(length))

    if check_var1.get() == "off":
        characters = characters.replace(string.ascii_uppercase, '')
    if check_var2.get() == "off":
        characters = characters.replace(string.ascii_lowercase, '')
    if check_var3.get() == "off":
        characters = characters.replace(string.digits, '')
    if check_var4.get() == "off":
        characters = characters.replace(custom_characters, '')
    if all(check_var.get() == "off" for check_var in (check_var1, check_var2, check_var3, check_var4)):
        result.configure(text="You must select at least one option")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result.configure(text=password)


root = CTk()
root.geometry("600x500")
root.resizable(False,False)

title = CTkLabel(master=root, text="Password generator", font=("Arial", 20), text_color="#F7DC6F")
title.place(relx=0.5, rely=0.1, anchor="center")


check_var1 = customtkinter.StringVar(value="on")
check_var2 = customtkinter.StringVar(value="on")
check_var3 = customtkinter.StringVar(value="on")
check_var4 = customtkinter.StringVar(value="on")
                                     
checkbox1 = CTkCheckBox(root, variable=check_var1, onvalue="on", offvalue="off", text="Capital letters (A-Z)", font=("Arial", 16), fg_color="#239B56", border_color="#707B7C", hover_color="trasnparent")
checkbox1.place(relx=0.1, rely=0.25, anchor=W)
checkbox2 = CTkCheckBox(root, variable=check_var2, onvalue="on", offvalue="off", text="Lowecase letters (a-z)", font=("Arial", 16), fg_color="#239B56", border_color="#707B7C", hover_color="trasnparent")
checkbox2.place(relx=0.1, rely=0.35, anchor=W)
checkbox3 = CTkCheckBox(root, variable=check_var3, onvalue="on", offvalue="off", text="Numbers (1-9)", font=("Arial", 16), fg_color="#239B56", border_color="#707B7C", hover_color="trasnparent")
checkbox3.place(relx=0.1, rely=0.45, anchor=W)
checkbox4 = CTkCheckBox(root, variable=check_var4, onvalue="on", offvalue="off", text="Custom characters (!#$%&/=*+@-~?)", font=("Arial", 16), fg_color="#239B56", border_color="#707B7C", hover_color="trasnparent")
checkbox4.place(relx=0.1, rely=0.55, anchor=W)

slider = CTkSlider(master=root, button_color="#6C3483", button_hover_color="#5B2C6F",from_=1, to=60, number_of_steps=59, command=sliding)
slider.place(relx=0.7, rely=0.25, anchor="center")
slider.set(1)
label_slider = customtkinter.CTkLabel(root, text="", font=("Arial", 15))
label_slider.place(relx=0.68, rely=0.3)

result = customtkinter.CTkLabel(root, text="", font=("Arial", 15))
result.place(relx=0.5, rely=0.8, anchor="center")

#Buttons
button = customtkinter.CTkButton(master=root, text="Generate password", command=generate_password, font=("Arial", 16), fg_color="#5B2C6F", hover_color="#512E5F", width=175, height=35)
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


root.mainloop()


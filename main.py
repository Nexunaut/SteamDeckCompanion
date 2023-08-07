from tkinter import *
import config_handler
import customtkinter

def Change_Style(*args):
    Update_Style(theme_var.get())
    
    
def Update_Style(theme):
    if theme == "light":
        customtkinter.set_appearance_mode("light")
    else:
        customtkinter.set_appearance_mode("dark")
    config_handler.save_settings(theme)

config = config_handler.load_settings()

sdc = customtkinter.CTk()

sdc.title("Steam Deck Companion")
sdc.geometry('1000x650')
sdc.resizable(False,False)

label_light_mode = customtkinter.CTkLabel(sdc, text="Light")
label_light_mode.place(x=865, y=19)

theme_var = customtkinter.StringVar(value=config["theme"])
Update_Style(config["theme"])
theme_switch = customtkinter.CTkSwitch(sdc, command=Change_Style, text="Dark", variable=theme_var, onvalue="dark", offvalue="light")
theme_switch.place(x=900, y=20) # Position the switch using pack

# optionmenu = customtkinter.CTkOptionMenu(sdc, corner_radius=5, values=["option 1", "option 2"])
# optionmenu.set("option 2")
# optionmenu.pack(pady=10) # Position the option menu using pack

sdc.mainloop()

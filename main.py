from tkinter import *
import config_handler
from device_info.get_device import FindDevice
from device_info.set_device import SetBrightness
import device_layout
import customtkinter

def Change_Style(*args):
    Update_Style(theme_var.get()) 
    
def Update_Style(theme):
    if theme == "light":
        customtkinter.set_appearance_mode("light")
    else:
        customtkinter.set_appearance_mode("dark")
    config_handler.save_settings(theme)

def UpdateBrightness(value):
    bValue = int(float(value))
    label.config(text=f"Brightness Value: {bValue} %")
    SetBrightness(bValue)
    
config = config_handler.load_settings()
devices = FindDevice()

connectedDevices= []

for device in devices:
    deck_type, device_id, serial_number, key_layout = device
    connectedDevices.append(deck_type + " [ " + serial_number + " ]")    
    print(key_layout)

sdc = customtkinter.CTk()

sdc.title("Stream Deck Companion")
sdcX = 1000
sdcY = 650
form_size = f"{sdcX}x{sdcY}"
sdc.geometry(form_size)
sdc.resizable(False,False)

device_frame = customtkinter.CTkFrame(sdc, fg_color="yellow", width=(sdcX-300), height=(sdcY - 150))

device_frame.place(x=0, y=150)
device_layout.load_content(device_frame)
# Handle theme selection
label_light_mode = customtkinter.CTkLabel(sdc, text="Light")
label_light_mode.place(x=865, y=19)

theme_var = customtkinter.StringVar(value=config["theme"])

Update_Style(config["theme"])

theme_switch = customtkinter.CTkSwitch(sdc, command=Change_Style, text="Dark", variable=theme_var, onvalue="dark", offvalue="light")
theme_switch.place(x=900, y=20) # Position the switch using pack

# Handle device connected



devicemenu = customtkinter.CTkOptionMenu(sdc, corner_radius=5, values=connectedDevices)
devicemenu.set("Select Device")
devicemenu.place(x=80, y=100) # Position the option menu using pack

slider = customtkinter.CTkSlider(sdc, from_=0, to=100, width=300, number_of_steps=20, command=UpdateBrightness)
slider.place(x=400, y=80)
label = Label(sdc, text="Brightness Value: 0%")
label.place(x=sdcX/2, y=100)

sdc.mainloop()

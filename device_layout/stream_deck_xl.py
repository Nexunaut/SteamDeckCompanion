from tkinter import Tk, Frame, Label
from customtkinter import CTkButton

def on_button_click(button_id):
    print(f"Button {button_id} was clicked")
    # You could also display the ID in the GUI, such as in a label:
    info_label.config(text=f"Button {button_id} was clicked")

def load_content(frame):
    global info_label  # Making the label accessible in on_button_click

    info_label = Label(frame, text="Click a button...")
    info_label.grid(row=4, column=0, columnspan=8)  # Spanning across 8 columns

    for row in range(4):
        for column in range(8):
            button_id = row * 8 + column  # Compute a unique ID for each button
            button = CTkButton(frame, text="", command=lambda b_id=button_id: on_button_click(b_id), width=72, height=72)
            button.grid(row=row, column=column, padx=5, pady=5)
            
            
    label_name = Label(frame, text="Name:")
    label_name.place(x=800, y=50")
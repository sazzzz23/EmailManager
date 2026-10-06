import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox

import message_manager as messages
import font_manager as fonts
from read_message import ReadMessage

from new_message import NewMessageGUI
from label_messages import LabelMessagesGUI

def set_text(text_area, content):
    text_area["state"] = "normal"
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)
    text_area["state"] = "disabled"


class EmailManager():
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x320")
        self.window.title("Email Manager")

        list_messages_btn = tk.Button(window, text="List Messages", command=self.list_messages)
        list_messages_btn.grid(row=0, column=0, padx=10, pady=10)

        read_message_btn = tk.Button(window, text="Read Message:", command=self.read_message)
        read_message_btn.grid(row=0, column=1, padx=10, pady=10)

        self.id_txt = tk.Entry(window, width=3)
        self.id_txt.grid(row=0, column=2, padx=10, pady=10)

        new_message_btn = tk.Button(window, text="New Message", command=self.new_message)
        new_message_btn.grid(row=0, column=3, padx=10, pady=10)

        label_messages_btn = tk.Button(window, text="Label Messages", command=self.label_messages)
        label_messages_btn.grid(row=0, column=4, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=60, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)


    def read_message(self):
        message_id_string = self.id_txt.get()
    valid = False

    if len(message_id_string) > 0:
        try:
            message_id = int(message_id_string)
            sender = messages.get_sender(message_id)

            if sender is not None:
                ReadMessage(tk.Toplevel(self.window), message_id)
                valid = True

        except ValueError:
            valid = False

    if not valid:
        messagebox.showinfo("WARNING", "You must select a valid message ID")

    self.status_lbl.configure(text="Read Message button was clicked!")

    def list_messages(self):
        message_list = messages.list_all()
        set_text(self.list_txt, message_list)
        self.status_lbl.configure(text="List Messages button was clicked!")

    def new_message(self):
        NewMessageGUI(tk.Toplevel(self.window))  # Open New Message GUI

    def label_messages(self):
        LabelMessagesGUI(tk.Toplevel(self.window))  # Open Label Messages GUI


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    EmailManager(window)
    window.mainloop()

import tkinter as tk
from tkinter import messagebox
import message_manager as msg_mgr

class LabelMessagesGUI:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Label Messages")
        self.parent.geometry("500x400")

        # Label Entry
        tk.Label(parent, text="Label:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.label_entry = tk.Entry(parent, width=30)
        self.label_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # List Messages Button
        list_btn = tk.Button(parent, text="List Messages", command=self.list_messages)
        list_btn.grid(row=0, column=2, padx=10, pady=10)

        # Message ID Entry
        tk.Label(parent, text="Message ID:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.id_entry = tk.Entry(parent, width=10)
        self.id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Add Label Button
        add_btn = tk.Button(parent, text="Add Label", command=self.add_label)
        add_btn.grid(row=1, column=2, padx=10, pady=10)

        # Message List Display
        self.list_txt = tk.Text(parent, width=60, height=15, wrap="none")
        self.list_txt.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Close Button
        close_btn = tk.Button(parent, text="Close", command=self.close)
        close_btn.grid(row=3, column=2, padx=10, pady=10)

    def add_label(self):
        try:
            message_id = int(self.id_entry.get())
            label = self.label_entry.get().strip()

            if msg_mgr.get_sender(message_id) is None:
                messagebox.showerror("Error", "Invalid message ID!")
            elif label == "":
                messagebox.showerror("Error", "Label cannot be empty!")
            else:
                msg_mgr.set_label(message_id, label)
                messagebox.showinfo("Success", "Label added!")
        except ValueError:
            messagebox.showerror("Error", "Message ID must be a number!")

    def list_messages(self):
        label = self.label_entry.get().strip()
        message_list = msg_mgr.list_all(label)
        self.list_txt.delete("1.0", tk.END)
        self.list_txt.insert(tk.END, message_list)

    def close(self):
        self.parent.destroy()
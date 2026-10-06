import tkinter as tk
from tkinter import messagebox
import message_manager as msg_mgr

class NewMessageGUI:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("New Message")
        self.parent.geometry("500x400")

        # Sender
        tk.Label(parent, text="From:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.sender_entry = tk.Entry(parent, width=40)
        self.sender_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Recipient
        tk.Label(parent, text="To:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.recipient_entry = tk.Entry(parent, width=40)
        self.recipient_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Subject
        tk.Label(parent, text="Subject:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.subject_entry = tk.Entry(parent, width=40)
        self.subject_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Content
        self.content_txt = tk.Text(parent, width=48, height=10, wrap="word")
        self.content_txt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Buttons
        send_btn = tk.Button(parent, text="Send", command=self.send)
        send_btn.grid(row=4, column=0, padx=10, pady=10)
        cancel_btn = tk.Button(parent, text="Cancel", command=self.close)
        cancel_btn.grid(row=4, column=1, padx=10, pady=10)

    def send(self):
        sender = self.sender_entry.get()
        recipient = self.recipient_entry.get()
        subject = self.subject_entry.get()
        content = self.content_txt.get("1.0", tk.END).strip()

        if sender == "" or recipient == "" or subject == "" or content == "":
            messagebox.showerror("Error", "All fields are required!")
            return

        msg_mgr.new_message(sender, recipient, subject, content)
        self.parent.destroy()

    def close(self):
        self.parent.destroy()
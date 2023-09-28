import tkinter as tk
from database import *
import random
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class PlayerEntry:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Software Gurus')

        # Create a label widget
        label = tk.Label(self.root, text="Enter your first name:")

        # Create a text box widget
        self.firstname_entry = tk.Entry(self.root)

        label1 = tk.Label(self.root, text="Enter your last name:")
        self.lastname_entry = tk.Entry(self.root)
        label2 = tk.Label(self.root, text="Enter your codename:")
        self.codename_entry = tk.Entry(self.root)

        display_database = tk.Button(self.root,text="Display database", command=self.display_database())
        # Create a button widget
        button = tk.Button(self.root, text="Add Player", command=self.add_player)
        # removebutton = tk.Button(self.root,text="Remove Player", command=self.remove_player)
        self.remove_entry = tk.Entry(self.root)
        # label3 = tk.Label(self.root,text="Remove a player:")

        # Add the widgets to the root window
        label.pack()
        self.firstname_entry.pack()
        label1.pack()
        self.lastname_entry.pack()
        label2.pack()
        self.codename_entry.pack()
        button.pack()
        display_database.pack()

        # Start the main event loop
        self.root.mainloop()

    def add_player(self):
        id = random.randint(10,99)
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        codename = self.codename_entry.get()
        add_entries(supabase,id,firstname,lastname,codename)

    # def remove_player(self, id):
    #     id = self.remove_entry.get()

    def display_database(self):
        print(supabase.table('player').select("*").execute())



# Create an instance of the NameGUI class
gui = PlayerEntry()



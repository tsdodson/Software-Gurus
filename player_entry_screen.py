import tkinter as tk
from database import *
import random
import os
import mysql.connector
from mysql.connector import Error
from udpclient import transmitEquipmentCode


load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class PlayerEntry:

    def createEntries(self):
        for row in range(15):
            label = tk.Label(self.frame, text=f"{row + 1}:")
            label.grid(row=row, column=0, sticky="e")

            entry = tk.Entry(self.frame)
            entry.grid(row=row, column=1)

            entry2 = tk.Entry(self.frame)
            entry2.grid(row=row, column=2)

            entry3 = tk.Entry(self.frame)
            entry3.grid(row=row, column=3)

            self.team1ID.append(entry)
            self.team1CodeName.append(entry2)
            self.team1EquipmentID.append(entry3)

        for row in range(15):
            label = tk.Label(self.frame, text=f"{row + 1}:")
            label.grid(row=row, column=4, sticky="e")

            entry = tk.Entry(self.frame)
            entry.grid(row=row, column=5)

            entry2 = tk.Entry(self.frame)
            entry2.grid(row=row, column=6)

            entry3 = tk.Entry(self.frame)
            entry3.grid(row=row, column=7)

            self.team2ID.append(entry)
            self.team2CodeName.append(entry2)
            self.team2EquipmentID.append(entry3)
        return
    
    def getInputs(self):
        self.team1Entries = []
        self.team2Entries = []
        for i in range(0,15):
            self.team1Entries.append([[self.team1ID[i].get()], [self.team1CodeName[i].get()], [self.team1EquipmentID[i].get()]])
            self.team2Entries.append([[self.team2ID[i].get()], [self.team2CodeName[i].get()], [self.team2EquipmentID[i].get()]])
        print(self.team1Entries, self.team2Entries)
        return 
    
    def add_player(self):
        self.getInputs()

        # add_entries(supabase,id,firstname,lastname,codename)
        # transmitEquipmentCode(id) # Change to equipment code
        return

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        self.root.title('Software Gurus - Laser Tag')
        
        self.team1ID = []
        self.team1CodeName = []
        self.team1EquipmentID = []

        self.team2ID = []
        self.team2CodeName = []
        self.team2EquipmentID = []

        # Create labels and entries
        self.createEntries()

        # Button when clicked, retrieves all information filled out
        add_player = tk.Button(self.root, text="Add Players", command=self.add_player)
        add_player.pack()

        # Start the main event loop
        self.root.mainloop()



# Create an instance of the NameGUI class
gui = PlayerEntry()






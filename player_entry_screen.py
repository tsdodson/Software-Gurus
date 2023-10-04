import tkinter as tk
from database import *
import random
import os
import mysql.connector
from mysql.connector import Error
from udpclient import transmitEquipmentCode
import random
import json
from tkinter.filedialog import asksaveasfile

first_names=('John','Andy','Joe')
last_names=('Johnson','Smith','Williams')

group=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(3))

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

path = './'
def writeToJSONFile(path, fileName, data):
    json.dump(data, path)

class PlayerEntry:

    def createEntries(self):
        for row in range(15):
            label = tk.Label(self.frame1, text=f"{row + 1}:")
            label.grid(row=row, column=0, sticky="e")

            entry = tk.Entry(self.frame1, width=7)
            entry.grid(row=row, column=1)

            entry2 = tk.Entry(self.frame1, width=15)
            entry2.grid(row=row, column=2)

            entry3 = tk.Entry(self.frame1, width=7)
            entry3.grid(row=row, column=3)

            entry4 = tk.Entry(self.frame1, width=15)
            entry4.grid(row=row, column=4)
            
            entry5 = tk.Entry(self.frame1, width=15)
            entry5.grid(row=row, column=5)
            self.team1ID.append(entry)
            self.team1CodeName.append(entry2)
            self.team1EquipmentID.append(entry3)
            self.team1FirstName.append(entry4)
            self.team1LastName.append(entry5)

        for row in range(15):
            label = tk.Label(self.frame1, text=f"{row + 1}:")
            label.grid(row=row, column=6, sticky="e")

            entry = tk.Entry(self.frame1, width=7)
            entry.grid(row=row, column=7)

            entry2 = tk.Entry(self.frame1, width=15)
            entry2.grid(row=row, column=8)

            entry3 = tk.Entry(self.frame1, width=7)
            entry3.grid(row=row, column=9)

            entry4 = tk.Entry(self.frame1, width=15)
            entry4.grid(row=row, column=10)

            entry5 = tk.Entry(self.frame1, width=15)
            entry5.grid(row=row,column=11)

            self.team2ID.append(entry)
            self.team2CodeName.append(entry2)
            self.team2EquipmentID.append(entry3)
            self.team2FirstName.append(entry4)
            self.team2LastName.append(entry5)

         # Button when clicked, retrieves all information filled out
        add_player = tk.Button(self.frame1, text="Add Players", command=self.add_player)
        add_player.grid(row=16, column=6)

        switch_button = tk.Button(self.frame1, text="F5 - Start Game", command=self.show_action_screen)
        switch_button.grid(row=17, column=6)

        self.current_frame = self.frame1
        self.frame1.grid(padx=50, pady=30, row=0, column=0, sticky="nsew")
        return
    
    # Creates action screen
    def createAction(self):
        label = tk.Label(self.frame2, text="Action Screen")
        label.grid(row=1, column=6, sticky="e")

        screen_switch = tk.Button(self.frame2, text="Esc - Exit", command=self.show_entry_screen)
        screen_switch.grid(row=16, column=6)
        return

    def show_entry_screen(self, event=None):
        if self.current_frame == self.frame2:
            self.frame2.grid_forget()  # Hide the current frame
            self.frame1.grid(padx=50, pady=30, row=0, column=0, sticky="nsew") # Show the next frame
            self.current_frame = self.frame1

    def show_action_screen(self, event=None):
        if self.current_frame == self.frame1:
            self.frame1.grid_forget()  # Hide the current frame
            self.frame2.grid(padx=50, pady=30, row=0, column=0, sticky="nsew") # Show the next frame
            self.current_frame = self.frame2

    # Transmits equipment
    def transmit(self):
        for entry in self.team1Entries:
            if entry[2] not in self.transmitted:
                transmitEquipmentCode(entry[2])
                self.transmitted.append(entry[2])
        for entry in self.team2Entries:
            if entry[2] not in self.transmitted:
                transmitEquipmentCode(entry[2])
                self.transmitted.append(entry[2])
        
    # Gets input and then calls transmit function
    def getInputsAndTransmit(self):
        
        for i in range(0,15):
            if self.team1ID[i].get() != '':
                self.team1Entries.append([self.team1ID[i].get(), self.team1CodeName[i].get(), self.team1EquipmentID[i].get(), self.team1FirstName[i].get(),self.team1LastName[i].get()])
                add_entries(supabase, self.team1ID[i].get(), self.team1FirstName[i].get(), self.team1LastName[i].get(),self.team1CodeName[i].get())
            if self.team2ID[i].get() != '':
                self.team2Entries.append([[self.team2ID[i].get()], [self.team2CodeName[i].get()], [self.team2EquipmentID[i].get()], [self.team2FirstName[i].get()],[self.team2LastName[i].get()]])
                add_entries(supabase, self.team2ID[i].get(), self.team2FirstName[i].get(), self.team2LastName[i].get(), self.team2CodeName[i].get())
            
        self.transmit()
        return 
    
    def add_player(self):
        self.getInputsAndTransmit()
        
        return

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1500x600")
        self.root.title('Software Gurus - Laser Tag')
        
        # Bind the '1' and '2' keys to switch between screens
        self.root.bind('<F5>', self.show_action_screen)
        self.root.bind('<Escape>', self.show_entry_screen)

        # Center the frames within the main window
        self.root.grid_columnconfigure(0, weight=1)

        self.frame1 = tk.Frame(self.root)
        

        self.frame2 = tk.Frame(self.root)
        self.current_frame = None
        
       
        # self.save = tk.Button(self.root,text="save player entries",command = self.check)
        # self.save.pack()

        self.transmitted = []

        self.team1Entries = []
        self.team2Entries = []

        self.team1FirstName = []
        self.team1LastName = []
        self.team1ID = []
        self.team1CodeName = []
        self.team1EquipmentID = []

        self.team2FirstName = []
        self.team2LastName = []
        self.team2ID = []
        self.team2CodeName = []
        self.team2EquipmentID = []

        # Create labels and entries for frame1
        self.createEntries()

        # Create action screen for frame2
        self.createAction()

        # Start the main event loop
        self.root.mainloop()

# Create an instance of the NameGUI class
gui = PlayerEntry()






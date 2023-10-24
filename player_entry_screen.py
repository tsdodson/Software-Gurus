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


load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

path = './'
def writeToJSONFile(path, fileName, data):
    json.dump(data, path)

class PlayerEntry:

    # ---------------------- Creates entry screen with all labels and entries ----------------------
    def createEntries(self):
        label = tk.Label(self.frame1, text="Player ID")
        label.grid(row=0, column = 1, sticky="e")
        label = tk.Label(self.frame1, text="Code Name")
        label.grid(row=0, column = 2, sticky="e")
        label = tk.Label(self.frame1, text="Equipment ID")
        label.grid(row=0, column = 3, sticky="e")
        label = tk.Label(self.frame1, text="Firstname")
        label.grid(row=0, column = 4, sticky="e")
        label = tk.Label(self.frame1, text="Lastname")
        label.grid(row=0, column = 5, sticky="e")

        label = tk.Label(self.frame1, text="Player ID")
        label.grid(row=0, column = 7, sticky="e")
        label = tk.Label(self.frame1, text="Code Name")
        label.grid(row=0, column = 8, sticky="e")
        label = tk.Label(self.frame1, text="Equipment ID")
        label.grid(row=0, column = 9, sticky="e")
        label = tk.Label(self.frame1, text="Firstname")
        label.grid(row=0, column = 10, sticky="e")
        label = tk.Label(self.frame1, text="Lastname")
        label.grid(row=0, column = 11, sticky="e")
        for row in range(1, 16):
            label = tk.Label(self.frame1, text=f"{row}:")
            label.grid(row=row, column=0, sticky="e")

            entry = tk.Entry(self.frame1, width=7)
            entry.grid(row=row, column=1)
            entry.configure(fg="white", bg="darkgreen")

            entry2 = tk.Entry(self.frame1, width=15)
            entry2.grid(row=row, column=2)
            entry2.configure(fg="white", bg="darkgreen")

            entry3 = tk.Entry(self.frame1, width=7)
            entry3.grid(row=row, column=3)
            entry3.configure(fg="white", bg="darkgreen")

            entry4 = tk.Entry(self.frame1, width=15)
            entry4.grid(row=row, column=4)
            entry4.configure(fg="white", bg="darkgreen")
            
            entry5 = tk.Entry(self.frame1, width=15)
            entry5.grid(row=row, column=5)
            entry5.configure(fg="white", bg="darkgreen")

            self.team1ID.append(entry)
            self.team1CodeName.append(entry2)
            self.team1EquipmentID.append(entry3)
            self.team1FirstName.append(entry4)
            self.team1LastName.append(entry5)

        for row in range(1, 16):
            select_entries(supabase, 10)
            label = tk.Label(self.frame1, text=f"{row}:")
            label.grid(row=row, column=6, sticky="e")

            entry = tk.Entry(self.frame1, width=7)
            entry.grid(row=row, column=7)
            entry.configure(fg="white", bg="maroon")

            entry2 = tk.Entry(self.frame1, width=15)
            entry2.grid(row=row, column=8)
            entry2.configure(fg="white", bg="maroon")

            entry3 = tk.Entry(self.frame1, width=7)
            entry3.grid(row=row, column=9)
            entry3.configure(fg="white", bg="maroon")

            entry4 = tk.Entry(self.frame1, width=15)
            entry4.grid(row=row, column=10)
            entry4.configure(fg="white", bg="maroon")

            entry5 = tk.Entry(self.frame1, width=15)
            entry5.grid(row=row,column=11)
            entry5.configure(fg="white", bg="maroon")

            self.team2ID.append(entry)
            self.team2CodeName.append(entry2)
            self.team2EquipmentID.append(entry3)
            self.team2FirstName.append(entry4)
            self.team2LastName.append(entry5)

         # Button when clicked, retrieves all information filled out
        add_player = tk.Button(self.frame1, text="Add Players", command=self.getInputsAndTransmit)
        add_player.grid(pady=20,row=16, column=4)

        # Button that switches to action screen
        switch_button = tk.Button(self.frame1, text="F5 - Start Game", command=self.show_action_screen)
        switch_button.grid(pady=20,row=16, column=5)

        # Button that clears entries
        clear_button = tk.Button(self.frame1, text="F12 - Clear Entries", command=self.clear_entries)
        clear_button.grid(pady=20, row=16, column=6)

        self.current_frame = self.frame1
        self.frame1.grid(padx=50, pady=30, row=0, column=0, sticky="nsew")
        return
    

    # ---------------------- Creates action screen ----------------------
    def createAction(self):
        label = tk.Label(self.frame2, text="Action Screen")
        label.grid(row=1, column=6, sticky="e")

        screen_switch = tk.Button(self.frame2, text="Esc - Exit", command=self.show_entry_screen)
        screen_switch.grid(row=16, column=6)
        return


    # ---------------------- Shows the entry screen in the window ----------------------
    def show_entry_screen(self, event=None):
        if self.current_frame == self.frame2:
            self.frame2.grid_forget()  # Hide the current frame
            self.frame1.grid(padx=50, pady=30, row=0, column=0, sticky="nsew") # Show the next frame
            self.current_frame = self.frame1


    # ---------------------- Shows the action screen in the window ----------------------
    def show_action_screen(self, event=None):
        if self.current_frame == self.frame1:
            self.frame1.grid_forget()  # Hide the current frame
            self.frame2.grid(padx=50, pady=30, row=0, column=0, sticky="nsew") # Show the next frame
            self.current_frame = self.frame2


    # ---------------------- Transmits equipment code ----------------------
    def transmit(self):
        for entry in self.team1Entries:
            if entry[2] not in self.transmitted:
                transmitEquipmentCode(entry[2])
                self.transmitted.append(entry[2])
        for entry in self.team2Entries:
            if entry[2] not in self.transmitted:
                transmitEquipmentCode(entry[2])
                self.transmitted.append(entry[2])


    # ---------------------- Gets input and then calls transmit function ----------------------
    def getInputsAndTransmit(self):
        for i in range(0,15):
            if self.team1ID[i].get() != '':
                if player_exists(supabase,self.team1ID[i].get()):
                    print('player already exists!')
                else:
                    self.team1Entries.append([self.team1ID[i].get(), self.team1CodeName[i].get(), self.team1EquipmentID[i].get(), self.team1FirstName[i].get(),self.team1LastName[i].get()])
                    add_entries(supabase, self.team1ID[i].get(), self.team1FirstName[i].get(), self.team1LastName[i].get(),self.team1CodeName[i].get())
            if self.team2ID[i].get() != '':
                if player_exists(supabase,self.team2ID[i].get()):
                    print('Player already exists!')
                else:
                    self.team2Entries.append([[self.team2ID[i].get()], [self.team2CodeName[i].get()], [self.team2EquipmentID[i].get()], [self.team2FirstName[i].get()],[self.team2LastName[i].get()]])
                    add_entries(supabase, self.team2ID[i].get(), self.team2FirstName[i].get(), self.team2LastName[i].get(), self.team2CodeName[i].get())
        self.transmit()
        return 
    
    # ---------------------- Clears all current entries ----------------------
    def clear_entries(self, event=None):
        # Iterate through the all the entries and clear the values
        for i in range(0,15):
            self.team1ID[i].delete(0, tk.END)
            self.team1CodeName[i].delete(0, tk.END)
            self.team1EquipmentID[i].delete(0, tk.END)
            self.team1FirstName[i].delete(0, tk.END)
            self.team1LastName[i].delete(0, tk.END)

            self.team2ID[i].delete(0, tk.END)
            self.team2CodeName[i].delete(0, tk.END)
            self.team2EquipmentID[i].delete(0, tk.END)
            self.team2FirstName[i].delete(0, tk.END)
            self.team2LastName[i].delete(0, tk.END)
        return 
    

    # ---------------------- Init function ----------------------
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1500x600")
        self.root.title('Software Gurus - Laser Tag')
        
        # Bind the 'F5', 'F12' and 'Escape' keys to perform operations
        self.root.bind('<F5>', self.show_action_screen)
        self.root.bind('<Escape>', self.show_entry_screen)
        self.root.bind('<F12>', self.clear_entries)
        
        # Center the frames within the main window
        self.root.grid_columnconfigure(0, weight=1)

        self.frame1 = tk.Frame(self.root)
        
        self.frame2 = tk.Frame(self.root)
        self.current_frame = None

        self.transmitted = [] # Holds codes that have been prev transmitted so they wont be transmitted already

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






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
            label = tk.Label(self.frame, text=f"{row + 1}:")
            label.grid(row=row, column=0, sticky="e")

            entry = tk.Entry(self.frame)
            entry.grid(row=row, column=1)

            entry2 = tk.Entry(self.frame)
            entry2.grid(row=row, column=2)

            entry3 = tk.Entry(self.frame)
            entry3.grid(row=row, column=3)

<<<<<<< HEAD
            entry4 = tk.Entry(self.frame)
            entry4.grid(row=row, column=4)
            
            entry5 = tk.Entry(self.frame)
            entry5.grid(row=row, column=5)
            self.team1ID.append(entry)
            self.team1CodeName.append(entry2)
            self.team1EquipmentID.append(entry3)
            self.team1FirstName.append(entry4)
            self.team1LastName.append(entry5)

        for row in range(15):
            label = tk.Label(self.frame, text=f"{row + 1}:")
            label.grid(row=row, column=6, sticky="e")

            entry = tk.Entry(self.frame)
            entry.grid(row=row, column=7)

            entry2 = tk.Entry(self.frame)
            entry2.grid(row=row, column=8)

            entry3 = tk.Entry(self.frame)
            entry3.grid(row=row, column=9)

            entry4 = tk.Entry(self.frame)
            entry4.grid(row=row, column=10)

            entry5 = tk.Entry(self.frame)
            entry5.grid(row=row,column=11)
=======
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
>>>>>>> 0601a24a11f56616ce1d7c80d04b58520048c24e

            self.team2ID.append(entry)
            self.team2CodeName.append(entry2)
            self.team2EquipmentID.append(entry3)
<<<<<<< HEAD
            self.team2FirstName.append(entry4)
            self.team2LastName.append(entry5)
=======
>>>>>>> 0601a24a11f56616ce1d7c80d04b58520048c24e
        return
    
    def getInputs(self):
        self.team1Entries = []
        self.team2Entries = []
        for i in range(0,15):
<<<<<<< HEAD
            self.team1Entries.append([[self.team1ID[i].get()], [self.team1CodeName[i].get()], [self.team1EquipmentID[i].get()], [self.team1FirstName[i].get()],[self.team1LastName[i].get()]])
            self.team2Entries.append([[self.team2ID[i].get()], [self.team2CodeName[i].get()], [self.team2EquipmentID[i].get()], [self.team2FirstName[i].get()],[self.team2LastName[i].get()]])
            add_entries(supabase, self.team1ID[i].get(), self.team1FirstName[i].get(), self.team1LastName[i].get(),self.team1CodeName[i].get())
            add_entries(supabase, self.team2ID[i].get(), self.team2FirstName[i].get(), self.team2LastName[i].get(), self.team2CodeName[i].get())
=======
            self.team1Entries.append([[self.team1ID[i].get()], [self.team1CodeName[i].get()], [self.team1EquipmentID[i].get()]])
            self.team2Entries.append([[self.team2ID[i].get()], [self.team2CodeName[i].get()], [self.team2EquipmentID[i].get()]])
>>>>>>> 0601a24a11f56616ce1d7c80d04b58520048c24e
        print(self.team1Entries, self.team2Entries)
        return 
    
    def add_player(self):
        self.getInputs()
        # add_entries(supabase,id,firstname,lastname,codename)
        # transmitEquipmentCode(id) # Change to equipment code
        return

    def __init__(self):
        self.root = tk.Tk()
<<<<<<< HEAD
        self.root.geometry("1500x600")
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        self.root.title('Software Gurus - Laser Tag')
        self.save = tk.Button(self.root,text="save player entries",command = self.check)
        self.save.pack()

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

        # Create labels and entries
        self.createEntries()

=======
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

>>>>>>> 0601a24a11f56616ce1d7c80d04b58520048c24e
        # Button when clicked, retrieves all information filled out
        add_player = tk.Button(self.root, text="Add Players", command=self.add_player)
        add_player.pack()

        # Start the main event loop
        self.root.mainloop()

<<<<<<< HEAD
    def check(self):
        data = {}
        id1 = [15]
        codename1 = [15]
        EqId1 = [15]
        firstname1 = [15]
        lastname1 = [15]
        id2 = [15]
        codename2 = [15]
        EqId2 = [15]
        firstname2 = [15]
        lastname2 = [15]
        for i in range(0,15):
            if(id1[i] == None and id2[i] == None):
                i = 15
            id1[i] = self.team1ID[i].get()
            codename1[i] = self.team1CodeName[i].get()
            EqId1[i] = self.team1EquipmentID[i].get()
            firstname1[i] = self.team1FirstName[i].get()
            lastname1[i] = self.team1LastName[i].get()
            id2[i] = self.team2ID[i].get()
            codename2[i] = self.team2CodeName[i].get()
            EqId2[i] = self.team2EquipmentID[i].get()
            firstname2[i] = self.team2FirstName[i].get()
            lastname2[i] = self.team2LastName[i].get()
            print(id1[i])
            print(codename1[i])
            print(EqId1[i])
            print(firstname1[i])
            print(lastname1[i])
            print(id2[i])
            print(codename2[i])
            print(EqId2[i])
            print(firstname2[i])
            print(lastname2[i])
            data['Team 1 ID'] = id1[i]
            data['Team 1 Codename'] = codename1[i]
            data['Team 1 Equipment ID'] = EqId1[i]
            data['Team 1 First Name'] = firstname1[i]
            data['Team 1 Last Name'] = lastname1[i]
            data['Team 2 ID'] = id2[i]
            data['Team 2 Codename'] = codename2[i]
            data['Team 2 Equipment ID'] = EqId2[i]
            data['Team 2 First Name'] = firstname2[i]
            data['Team 2 Last Name'] = lastname2[i]
        files = [('JSON File', '*.json')]
        fileName = 'ENTRIES'
        filepos = asksaveasfile(filetypes = files, defaultextension = json, initialfile = 'ENTRIES')
        writeToJSONFile(filepos,fileName,data)

=======
>>>>>>> 0601a24a11f56616ce1d7c80d04b58520048c24e


# Create an instance of the NameGUI class
gui = PlayerEntry()






import threading
import tkinter as tk
from tkinter import messagebox
import pygame
from database import *
import random
import os
import mysql.connector
from mysql.connector import Error
from udpclient import transmitCode
from udpclient import returnReceivedMessages
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
        for widget in self.frame2.winfo_children():
            if hasattr(widget, 'grid_info') and 'column' in widget.grid_info():
                if widget.grid_info()["column"] in [1, 2, 40, 41]:
                    widget.destroy()
        label = tk.Label(self.frame2, text="Action Screen")
        label.grid(row=1, column=6, sticky="e")

        label = tk.Label(self.frame2, text= "GREEN TEAM")
        label.grid(row= 2, column=1, sticky= "e")
        label = tk.Label(self.frame2, text= "RED TEAM")
        label.grid(row= 2, column=40, sticky= "e")

        self.team1Entries.sort(key=lambda x: x[5], reverse=True)
        self.team2Entries.sort(key=lambda x: x[5], reverse=True)
        for i in range(len(self.team1Entries)):
            label = tk.Label(self.frame2, text= self.team1Entries[i][1])
            label.grid(row= 3 + i, column=1, sticky= "e")                    
            
        for i in range(len(self.team1Entries)):
            label = tk.Label(self.frame2, text= self.team1Entries[i][5])
            label.grid(row= 3 + i, column=2, sticky= "e")


        for i in range(len(self.team2Entries)):
            label = tk.Label(self.frame2, text= self.team2Entries[i][1])
            label.grid(row= 3 + i, column=40, sticky= "e")
            
        for i in range(len(self.team2Entries)):
            label = tk.Label(self.frame2, text= self.team2Entries[i][5])
            label.grid(row= 3 + i, column=41, sticky= "e")
        
        #Team Scores
        for i in range(len(self.team1Entries)):
            label = tk.Label(self.frame2, text = self.team1Score)
            label.configure(fg= "black")
            label.grid(row= 20, column=2, sticky= "e")
            if self.team1Score > self.team2Score:
                label.configure(fg= "red",font=(20))

        for i in range(len(self.team2Entries)):
            label = tk.Label(self.frame2, text = self.team2Score)
            label.configure(fg= "black")
            label.grid(row= 20, column=41, sticky= "e")
            if self.team2Score > self.team1Score:
                label.configure(fg= "red",font=(20))
                
        label = tk.Label(self.frame2, text = "Events")
        label.grid(row=24,  column=6, sticky="e")

        screen_switch = tk.Button(self.frame2, text="Esc - Exit", command=self.show_entry_screen)
        screen_switch.grid(row=1, column=20)
            

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
            self.countdown_timer()


    # ---------------------- Transmits equipment code ----------------------
    def transmit(self):
        for entry in self.team1Entries:
            if entry[2] not in self.transmitted:
                transmitCode(entry[2])
                self.transmitted.append(entry[2])
        for entry in self.team2Entries:
            if entry[2] not in self.transmitted:
                transmitCode(entry[2])
                self.transmitted.append(entry[2])


    # ---------------------- Gets input and then calls transmit function ----------------------
    def getInputsAndTransmit(self):
        for i in range(0,15):
            if self.team1ID[i].get() != '':
                if player_exists(supabase,self.team1ID[i].get()):
                    print('player already exists!')
                else:
                    self.team1Entries.append([self.team1ID[i].get(), self.team1CodeName[i].get(), self.team1EquipmentID[i].get(), self.team1FirstName[i].get(),self.team1LastName[i].get(),0])
                    add_entries(supabase, self.team1ID[i].get(), self.team1FirstName[i].get(), self.team1LastName[i].get(),self.team1CodeName[i].get())
            if self.team2ID[i].get() != '':
                if player_exists(supabase,self.team2ID[i].get()):
                    print('Player already exists!')
                else:
                    self.team2Entries.append([self.team2ID[i].get(), self.team2CodeName[i].get(), self.team2EquipmentID[i].get(), self.team2FirstName[i].get(),self.team2LastName[i].get(),0])
                    add_entries(supabase, self.team2ID[i].get(), self.team2FirstName[i].get(), self.team2LastName[i].get(), self.team2CodeName[i].get())
        self.transmit()
        # Create action screen for frame2
        self.createAction()
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
    
    
        
    def updateEvents(self):
        self.numevents+=1
        # label = tk.Text(self.frame2, text = "")
        # label.grid(row=25+self.numevents,  column=6, sticky="e", columnspan=12, rowspan=20)
        msg = returnReceivedMessages()
        if msg == "":
            return
        else:
            player1 = ""
            player2 = ""
            team1 = ''
            team2 = ''
            base1 = 'Green'
            base2 = 'Red'
            
            r, t, h = 0, "", ""

            while r < len(msg) and msg[r] != ':' :
                t += msg[r]
                r+=1
            r+= 1
            h = msg[r:]
            
            transmitCode(h)
            score1Index,score2Index = 0,0
            for i in range(max(len(self.team1Entries), len(self.team2Entries))):
                if t == self.team1Entries[i][2]:
                    player1 = self.team1Entries[i][1]
                    team1 = 'Green'
                    score1Index = i
                    break
                elif t == self.team2Entries[i][2]:
                    player1 = self.team2Entries[i][1]
                    team1 = 'Red'
                    score1Index = i
                    break
            for i in range(max(len(self.team1Entries), len(self.team2Entries))):
                if h == self.team1Entries[i][2]:
                    player2 = self.team1Entries[i][1]
                    team2 = 'Green'
                    score2Index = i
                    break
                elif h == self.team2Entries[i][2]:
                    player2 = self.team2Entries[i][1]
                    team2 = 'Red'
                    score2Index = i
                    break
            if team1 == team2:
                transmitCode(t)
                self.text.insert(tk.END, "Friendly fire!\n")
            elif player1 and player2:
                self.text.insert(tk.END, f"{player1} shot {player2}\n")
                if team1 == "Green":
                    self.team1Entries[score1Index][5] += 10
                    self.team1Score += 10
                if team1 == "Red":
                    self.team2Entries[score1Index][5] += 10
                    self.team2Score += 10
                    
            if h in ['43', '53']:
                if h == '53':
                    if player1 and team1 == 'Green':
                        self.text.insert(tk.END, f"{player1} shot Red Base\n")
                        if "🅱️" not in self.team1Entries[score1Index][1]:
                            self.team1Entries[score1Index][1] = "🅱️" + self.team1Entries[score1Index][1]
                        self.team1Entries[score1Index][5] += 100
                        self.team1Score += 100
                elif h == '43':
                    if player1 and team1 == 'Red':
                        self.text.insert(tk.END, f"{player1} shot Green Base\n")
                        if "🅱️" not in self.team2Entries[score1Index][1]:
                            self.team2Entries[score1Index][1] = "🅱️" + self.team2Entries[score1Index][1]
                        self.team2Entries[score1Index][5] += 100
                        self.team2Score += 100
                    
        self.createAction()

    def game_timer(self):
        countdown_seconds = 360
        def update_game_timer():
            nonlocal countdown_seconds
            if countdown_seconds > 0:
                countdown_seconds -= 1
                self.updateEvents()
                timer_label.grid(row=1, column=15)
                timer_label.after(1000, update_game_timer)
                timer_label.config(text=f"Time remaining: {countdown_seconds}")
            else:
                transmitCode("221")
                transmitCode("221")
                transmitCode("221")
                timer_label.destroy()
            


        timer_label = tk.Label(self.frame2, text=f"Game ends in {countdown_seconds}")
        
        update_game_timer()
    
    def countdown_timer(self):
        countdown_seconds = 30
        random_track = random.randint(1,8)
        mp3_file_path = "./GameMusicFiles/Track0" + str(random_track) + ".mp3"


    # Create a function to update the timer label
        def update_timer():
            nonlocal countdown_seconds
            if countdown_seconds > 0:        
                if countdown_seconds == 17:
                    self.play_mp3(mp3_file_path)
                countdown_seconds -= 1
                timer_label.grid(row=18, column=5)
                timer_label.after(1000, update_timer)
                timer_label.config(text=f"Game starting in {countdown_seconds}")
            else:
                transmitCode("202")
                self.frame1.grid_forget()  # Hide the current frame
                self.frame2.grid(padx=50, pady=30, row=0, column=0, sticky="nsew") # Show the next frame
                self.current_frame = self.frame2
                timer_label.destroy()
                self.game_timer()
                
        timer_label = tk.Label(self.frame1, text=f"Game starting in {countdown_seconds}")
                
        # Start the timer
        update_timer()

        #root.mainloop()
        
    def play_mp3(self, file_path):
                def play_music():
                    try:
                        pygame.mixer.init()
                        # Load the MP3 file
                        pygame.mixer.music.load(file_path)

                        # Play the MP3 file
                        pygame.mixer.music.play()

                        # Wait for the music to finish playing
                        while pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(10)

                    except pygame.error as e:
                        print(f"Error playing MP3: {e}")

                # Create a new thread for playing music
                music_thread = threading.Thread(target=play_music)

                # Start the thread
                music_thread.start()

    # ---------------------- Init function ----------------------
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1500x600")
        self.root.title('Software Gurus - Laser Tag')
        self.numevents = 0
        

        # Bind the 'F5', 'F12' and 'Escape' keys to perform operations
        self.root.bind('<F5>', self.show_action_screen)
        self.root.bind('<Escape>', self.show_entry_screen)
        self.root.bind('<F12>', self.clear_entries)
        
        # Center the frames within the main window
        self.root.grid_columnconfigure(0, weight=1)

        self.frame1 = tk.Frame(self.root)
        
        self.frame2 = tk.Frame(self.root)
        self.current_frame = None
        self.text = tk.Text(self.frame2, wrap=tk.WORD, width=50, height=10)
        self.text.grid(row= 25,column=6)
        self.scrollbar = tk.Scrollbar(self.frame2, command=self.text.yview)
        self.scrollbar.grid(row=25,column=7)
        self.text.config(yscrollcommand=self.scrollbar.set)

        self.transmitted = [] # Holds codes that have been prev transmitted so they wont be transmitted already

        self.team1Entries = []
        self.team2Entries = []

        self.team1FirstName = []
        self.team1LastName = []
        self.team1ID = []
        self.team1CodeName = []
        self.team1EquipmentID = []
        self.team1PlayerScore = []
        self.team1Score = 0

        self.team2FirstName = []
        self.team2LastName = []
        self.team2ID = []
        self.team2CodeName = []
        self.team2EquipmentID = []
        self.team2PlayerScore = []
        self.team2Score = 0        

        # Create labels and entries for frame1
        self.createEntries()

        
        
        
        # Start the main event loop
        self.root.mainloop()
    


# Create an instance of the NameGUI class
gui = PlayerEntry()






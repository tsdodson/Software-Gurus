import tkinter as tk

class PlayerEntry:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Software Gurus')

        # Create a label widget
        label = tk.Label(self.root, text="Enter your name:")

        # Create a text box widget
        self.player_entry = tk.Entry(self.root)

        # Create a button widget
        button = tk.Button(self.root, text="Add Player", command=self.add_player)

        # Add the widgets to the root window
        label.pack()
        self.player_entry.pack()
        button.pack()

        # Start the main event loop
        self.root.mainloop()

    def add_player(self):
        player = self.player_entry.get()
        print(player, 'added')

# Create an instance of the NameGUI class
gui = PlayerEntry()


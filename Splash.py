import tkinter as tk
from tkinter import PhotoImage
import time

class Splash(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x255")
        self.title("Splash Screen")
        self.overrideredirect(True)  # Remove window borders and decorations
        self.configure(bg="white")

        # Load the image
        self.splash_image = PhotoImage(file="images/logo.gif")  # Make sure you have a GIF image

        # Center the splash screen on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_reqwidth()) / 2
        y = (screen_height - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))

        # Create a label to display the image
        self.splash_label = tk.Label(self, image=self.splash_image, bg="white")
        self.splash_label.pack()

        # Update the splash screen
        self.update()
        self.after(3000, self.destroy_splash)  # Close the splash screen after 3000ms (3 seconds)

    def destroy_splash(self):
        self.destroy()

if __name__ == "__main__":
    splash = Splash()
    splash.mainloop()

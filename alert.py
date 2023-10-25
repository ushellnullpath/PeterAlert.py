'''
Project: PeterAlert
By: ushellnullpath
Description:
A meme project.
Different libraries that have been used are tkinter, pillow, and pygame.
Last updated on (D/M/Y): 26/10/2023
'''

from tkinter import *
from PIL import ImageTk, Image
import pygame


class PeterAlert:
    def __init__(self):
        self.root = Tk()
        self.root.title("Peter Alert")
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', 1)

        # window dimensions and positioning
        self.width_of_win = 382
        self.height_of_win = 272
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coord = ((self.screen_width/2) - (self.width_of_win/2))
        self.y_coord = ((self.screen_height/2) - (self.height_of_win/2))
        self.root.geometry(("%dx%d+%d+%d") % (self.width_of_win,
                           self.height_of_win, self.x_coord, self.y_coord))

        # title and close button
        self.title_frame = Frame(self.root, bg='white',)
        self.title = Label(self.title_frame, text='Peter Alert', font=(
            'Segoe UI', 14), bg='white', fg='black')
        self.title.pack(side=LEFT, padx=5)
        self.exit_button = Button(self.title_frame, text='❌', font=(
            'Segoe UI', 12), bd=0, bg='white', fg='black', command=self.root.quit)
        self.exit_button.pack(side=RIGHT, pady=2, padx=2)
        self.title_frame.pack(anchor=N, fill=X)

        # displaying the Peter Griffin image
        self.img = Image.open("images/peter_griffin.png")
        self.resized_img = self.img.resize((125, 125))
        self.tk_img = ImageTk.PhotoImage(self.resized_img)
        self.img_label = Label(self.root, image=self.tk_img)
        self.img_label.place(relx=0.5, rely=0.45, anchor='center')

        # OK button
        self.ok_button = Button(self.root, text="OK", width=10, font=('Segoe UI', 12), foreground='#000000',
                                background='#ffffff', command=self.root.quit)
        self.ok_button.place(relx=0.5, rely=0.8, anchor='center')

        # initializing and playing the Peter Griffin laugh
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/peter_griffin_laugh.mp3")
        pygame.mixer.music.play(loops=-1)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    alert = PeterAlert()
    alert.run()

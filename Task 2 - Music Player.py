# create a Music Player using Tkinter, Pygame and Pillow
import pygame
from pygame import mixer
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Initialize the mixer module
pygame.mixer.init()

# Create the main window
app = Tk()
app.title("Music Player")
app.geometry("477x400")
app.config(bg="black")

# open image
pic=Image.open("./cd.jpg")

# resize and paste the image
resized=pic.resize((240, 180), Image.Resampling.LANCZOS)

new_pic=ImageTk.PhotoImage(resized)

label=Label(app, image=new_pic, bg="black")
label.place(x=15, y=15)

# Create a list of songs
songs_list = Listbox(app, width=32, height=11, bg="black", fg="white")
songs_list.place(x=270, y=16)

# add songs to the playlist
def addsongs():
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))
    for s in temp_song:
        s = s.replace("C:/Users/shafi/Music/", "")
        songs_list.insert(END, s)

# delete a song
def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])

# play a song
def Play():
    song = songs_list.get(ACTIVE)
    song = f'C:/Users/shafi/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()

# pause a song
def Pause():
    mixer.music.pause()

# resume
def Resume():
    mixer.music.unpause()

# navigate to the previous song
def Previous():
    previous_one = songs_list.curselection()
    previous_one = previous_one[0] - 1
    temp2 = songs_list.get(previous_one)
    temp2 = f'C:/Users/shafi/Music/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)

# navigate to the next song
def Next():
    next_one = songs_list.curselection()
    next_one = next_one[0] + 1
    temp = songs_list.get(next_one)
    temp = f'C:/Users/shafi/Music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(next_one)
    songs_list.selection_set(next_one)

# Create buttons
add_button = Button(app, text="Add", font=("Helvetica", 12), command=addsongs, bg="blue", fg="white", border=0).place(x=270, y=197)

delete_button = Button(app, text="Delete", font=("Helvetica", 12), command=deletesong, bg="blue", fg="white", border=0).place(x=320, y=197)

play_image=PhotoImage(file="play_img.png")
play_button = Button(app, text="Play", image=play_image, command=Play, bg="black", border=0).place(x=110, y=320)

pause_image=PhotoImage(file="pause_img.png")
pause_button = Button(app, text="Pause", image=pause_image, command=Pause, bg="black", border=0).place(x=200, y=318)

resume_image=PhotoImage(file="resume_img.png")
resume_button = Button(app, text="resume", image=resume_image, command=Resume, bg="black", border=0).place(x=300, y=320)

prev_image=PhotoImage(file="prev_img.png")
prev_button = Button(app, text="<", image=prev_image, command=Previous, bg="black", border=0).place(x=20, y=317)

next_image=PhotoImage(file="next_img.png")
next_button = Button(app, text=">", image=next_image, command=Next, bg="black", border=0).place(x=390, y=317)

# Volume control
volume_slider = Scale(app, from_=0, to=100, length=470, orient=HORIZONTAL, command=lambda v: mixer.music.set_volume(int(v) / 100), bg="black", fg="white",troughcolor="grey", sliderrelief="flat", highlightbackground="black", highlightcolor="black")
volume_slider.set(40)
volume_slider.place(x=0, y=270)

# execute tkinter
app.mainloop()
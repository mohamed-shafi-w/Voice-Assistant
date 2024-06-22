# Creating a assistant using tkinter, speech recognition, pillow, pywhatkit, webbrowser, subprocess and wikipedia
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import subprocess
import sys
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from PIL import ImageTk, Image

# initialize
listener = sr.Recognizer()
engine = pyttsx3.init()

# for female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# for speech
def talk(text):
    engine.say(text)
    engine.runAndWait()

# for giving input
def input_instruction():
    try:
        with sr.Microphone() as origin:
            print('Listening...')
            voice = listener.listen(origin)
            instruction = listener.recognize_google(voice)
            instruction = instruction.lower()
            if "nikitha" in instruction:
                instruction = instruction.replace('nikitha', '')
                print(instruction)
            return instruction
    except sr.UnknownValueError:
        talk("Sorry, I did not catch that")
        return ""
    except sr.RequestError:
        talk("Sorry, my speech service is down")
        return ""

def process_instruction(instruction):
    output_text.insert(tk.END, f'{instruction}\n')
    output_text.yview(tk.END)
    print(instruction)
    
    # playing song in youtube
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("playing " + song)
        output_text.insert(tk.END, f'~ Playing {song}\n\n')
        output_text.yview(tk.END)
        pywhatkit.playonyt(song)

    elif 'hello zarina' in instruction or 'hello' in instruction:
        talk("Hello. How can I assist you?")
        output_text.insert(tk.END, '~ Hello, How can I assist you?\n\n')
        output_text.yview(tk.END)

    elif 'nice to meet you' in instruction or 'nice to meet you zarina' in instruction:
        talk('i am glad you enjoyed meeting me. i hope that as we get to know each other your enjoyment intensifies')
        output_text.insert(tk.END, "~ I'm glad you enjoyed meeting me. I hope that as we get to know each other your enjoyment intensifies\n\n")
        output_text.yview(tk.END)
    
    elif 'what about you' in instruction or 'how are you zarina' in instruction:
        talk('I am good. what about you?')
        output_text.insert(tk.END, '~ I am good, what about you?\n\n')
        output_text.yview(tk.END)

    elif 'yeah i am also fine' in instruction or 'yeah i am also good' in instruction or 'i am fine' in instruction:
        talk('glad to hear that')
        output_text.insert(tk.END, '~ Glad to hear that\n\n')
        output_text.yview(tk.END)

    elif 'i need your help' in instruction or 'can you help me' in instruction:
        talk('of course. i am here to help. what do you need assistance with')
        output_text.insert(tk.END, "Of Course!, I'm here to help. What do you need assistance with?\n\n")
        output_text.yview(tk.END)
    
    elif 'what is your name' in instruction or 'your name' in instruction:
        talk("I am zarina. How can I assist you?")
        output_text.insert(tk.END, "~ I am Zarina, How can I assist you?\n\n")
        output_text.yview(tk.END)
    
    elif 'what is' in instruction or 'define' in instruction:
        topic = instruction.replace("what is", "").replace('define', "").strip()
        info = wikipedia.summary(topic, sentences=1)
        print(info)
        talk(info)
        output_text.insert(tk.END, f'~ {info}\n\n')
        output_text.yview(tk.END)

    # asking time
    elif "what's the time now" in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time ' + time)
        output_text.insert(tk.END, f'~ Current time {time}\n\n')
        output_text.yview(tk.END)
    
    # asking date
    elif "what is today's date" in instruction or "what is the date today" in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%y')
        talk("Today's date " + date)
        output_text.insert(tk.END, f'~ Today\'s date {date}\n\n')
        output_text.yview(tk.END)

    # asking questions
    elif 'who is' in instruction:
        human = instruction.replace('who is', "")
        info = wikipedia.summary(human, sentences=1)
        print(info)
        talk(info)
        output_text.insert(tk.END, f'~ {info}\n\n')
        output_text.yview(tk.END)

     # opening notepad
    elif 'open notepad' in instruction:
        talk('opening notepad')
        output_text.insert(tk.END, '~ opening notepad\n\n')
        output_text.yview(tk.END)
        subprocess.Popen('notepad.exe')

    # opening command prompt
    elif 'open command prompt' in instruction:
        talk('opening command')
        output_text.insert(tk.END, '~ opening command prompt\n\n')
        output_text.yview(tk.END)
        subprocess.Popen('cmd.exe')

    # opening youtube
    elif 'open youtube' in instruction or 'go to youtube' in instruction:
        talk('opening youtube')
        output_text.insert(tk.END, '~ opening youtube\n\n')
        output_text.yview(tk.END)
        webbrowser.open("https://www.youtube.com")
    
    # opening google
    elif 'open google' in instruction or 'go to google' in instruction:
        talk('opening google')
        output_text.insert(tk.END, '~ opening google\n\n')
        output_text.yview(tk.END)
        webbrowser.open("https://www.google.com")
    
    # searching particular from web
    elif 'search' in instruction or 'search about' in instruction:
        topic = instruction.replace('search', "").replace('search about', "").strip()
        talk("searching " + topic)
        output_text.insert(tk.END, f'~ Searching {topic}\n\n')
        output_text.yview(tk.END)
        pywhatkit.search(topic)

    # opening gmail
    elif 'open gmail' in instruction or 'go to gmail' in instruction:
        talk('opening gmail')
        output_text.insert(tk.END, '~ opening gmail\n\n')
        output_text.yview(tk.END)
        webbrowser.open("https://mail.google.com")

    elif 'ok bye' in instruction or "bye" in instruction:
        talk('good bye. if you have any questions or tasks, feel free to ask anytime')
        output_text.insert(tk.END, '~ Goodbye!, If you have any questions or tasks, feel free to ask anytime')
        output_text.yview(tk.END)
        sys.exit()

    else:
        talk("Sorry I can't understand")
        output_text.insert(tk.END, "~ Sorry I can't understand\n\n")
        output_text.yview(tk.END)

def play_zarina():
    output_text.insert(tk.END, "Listening...\n\n")
    output_text.yview(tk.END)
    root.update_idletasks()
    instruction = input_instruction()
    process_instruction(instruction)

def send_instruction():
    instruction = text_entry.get()
    text_entry.delete(0, tk.END)
    process_instruction(instruction)

# creating a new window
def open_main_window():
    new_window = tk.Toplevel(root)
    new_window.title("Zarina - Voice Assistant")
    new_window.geometry("344x620")
    new_window.config(bg="#565756")
    new_window.resizable(False, False)

    # resize image
    new_image = Image.open("./Zarina.png")
    resized_new_image = new_image.resize((340, 425), Image.Resampling.LANCZOS)
    new_image_pic = ImageTk.PhotoImage(resized_new_image)

    # insert image
    new_image_label = tk.Label(new_window, image=new_image_pic, bg="black")
    new_image_label.place(x=0, y=0)
    new_image_label.image = new_image_pic

    global output_text
    # create scrolled text to display output
    output_text = scrolledtext.ScrolledText(new_window, width=32, height=6, wrap=tk.WORD, bg="black", fg="white", border = 1)
    output_text.place(x=1, y=430)

    global text_entry
    # create entry for text
    text_entry = tk.Entry(new_window, width=17, bg="white", fg="black", font=("Helvetica", 13))
    text_entry.place(x=76, y=570)

    # resize image
    send_image = Image.open("./send_image.png")
    resized_send_image = send_image.resize((86, 86), Image.Resampling.LANCZOS)
    send_image_pic = ImageTk.PhotoImage(resized_send_image)

    # create send button
    send_button = tk.Button(new_window, text="Send", image = send_image_pic, border = 0, command=send_instruction, width=73, height=63, bg="#565756", fg="white")
    send_button.place(x=275, y=554)
    send_button.image = send_image_pic

    # resize image
    talk_image = Image.open("./mic_img.png")
    resized_talk_image = talk_image.resize((95, 90), Image.Resampling.LANCZOS)
    talk_image_pic = ImageTk.PhotoImage(resized_talk_image)

    # create talk button
    talk_button = tk.Button(new_window, text="Talk", image = talk_image_pic, border=0, command=play_zarina, width=70, height=70, bg="#565756", fg="white")
    talk_button.place(x=1, y=555)
    talk_button.image = talk_image_pic

    root.withdraw()

# for loading bar
def start_loading():
    progress['value'] = 0
    root.after(100, update_progress, 0)

def update_progress(value):
    if value < 100:
        progress['value'] = value
        root.after(50, update_progress, value + 1)
    else:
        open_main_window()

# creating a window
root = tk.Tk()
root.title("Zarina - Voice Assistant")
root.geometry("344x620")
root.config(bg="white")
root.resizable(False, False)

# resize and paste logo
pic = Image.open("./Zarina Logo.png")
resized = pic.resize((145, 45), Image.Resampling.LANCZOS)
new_pic = ImageTk.PhotoImage(resized)

label = tk.Label(root, image=new_pic, bg="white")
label.place(x=100, y=230)

# progress bar
progress = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress.place(x=75, y=340)

# info
info_label=tk.Label(root, text="© 2024 Zarina. All rights reserved.", bg="white", fg="black", font=("Helvetica", 9))
info_label.place(x=65, y=460)

start_loading()

# execute tkinter
root.mainloop()
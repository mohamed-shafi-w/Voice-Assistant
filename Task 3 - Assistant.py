# Creating a assistant using tkinter, speech recognition, pillow, pywhatkit, webbrowser, subprocess and wikipedia
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import subprocess
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
        talk("Hello, How can I assist you?")
        output_text.insert(tk.END, '~ Hello, How can I assist you?\n\n')
        output_text.yview(tk.END)

    elif 'zarina' in instruction or 'zari' in instruction:
        talk("yeah its me, How can I help you?")
        output_text.insert(tk.END, "~ Yeah it's me, How can I help you?\n\n")
        output_text.yview(tk.END)

    elif 'hi zarina' in instruction or 'hi' in instruction:
        talk("Hi, How can I assist you?")
        output_text.insert(tk.END, '~ Hi, How can I assist you?\n\n')
        output_text.yview(tk.END)

    elif 'can i call you as zari' in instruction:
        talk("sure, you can call me zari")
        output_text.insert(tk.END, '~ Sure, You can call me Zari\n\n')
        output_text.yview(tk.END)
    
    # asking time
    elif "what's the time now" in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time ' + time)
        output_text.insert(tk.END, f'~ Current time {time}\n\n')
        output_text.yview(tk.END)

    elif 'what is your age' in instruction or 'your age' in instruction:
        talk("I don't have an age in the human sense, since I'm an Artificial Intelligence. I was first released in June 2024")
        output_text.insert(tk.END, "~ I don't have an age in the human sense since I'm an Artificial Intelligence. I was first released in June 2024\n\n")
        output_text.yview(tk.END)
    
    # asking date
    elif "what is today's date" in instruction or "what is the date today" in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%y')
        talk("Today's date " + date)
        output_text.insert(tk.END, f'~ Today\'s date {date}\n\n')
        output_text.yview(tk.END)
    
    elif 'how are you' in instruction:
        talk('I am well, what about you?')
        output_text.insert(tk.END, '~ I am well, what about you?\n\n')
        output_text.yview(tk.END)

    elif 'who are you' in instruction:
        talk('I am zarina, your smart companion')
        output_text.insert(tk.END, "~ I am Zarina, Your Smart Companion\n\n")
        output_text.yview(tk.END)
    
    elif 'what is your name' in instruction or 'your name' in instruction:
        talk("I am zarina, How can I assist you?")
        output_text.insert(tk.END, "~ I am Zarina, How can I assist you?\n\n")
        output_text.yview(tk.END)

    elif 'i love you zarina' in instruction or 'i love you' in instruction:
        talk("i love you too")
        output_text.insert(tk.END, "~ I love you too\n\n")
        output_text.yview(tk.END)
    
    # asking questions
    elif 'who is' in instruction:
        human = instruction.replace('who is', "")
        info = wikipedia.summary(human, sentences=1)
        print(info)
        talk(info)
        output_text.insert(tk.END, f'~ {info}\n\n')
        output_text.yview(tk.END)
    
    elif 'what is' in instruction or 'define' in instruction:
        topic = instruction.replace("what is", "").replace('define', "").strip()
        info = wikipedia.summary(topic, sentences=1)
        print(info)
        talk(info)
        output_text.insert(tk.END, f'~ {info}\n\n')
        output_text.yview(tk.END)
    
    # searching particular from web
    elif 'search' in instruction:
        topic = instruction.replace('search', "").strip()
        talk("searching " + topic)
        output_text.insert(tk.END, f'~ Searching {topic}\n\n')
        output_text.yview(tk.END)
        pywhatkit.search(topic)
    
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

    # opening MS edge
    elif 'open microsoft edge' in instruction or 'go to microsoft edge' in instruction:
        talk('opening microsoft edge')
        output_text.insert(tk.END, '~ opening microsoft edge\n\n')
        output_text.yview(tk.END)
        webbrowser.open("https://www.msn.com/en-in/feed?ocid=wn_startbrowsing&form=MT00PF")

    # opening gmail
    elif 'open gmail' in instruction or 'go to gmail' in instruction:
        talk('opening gmail')
        output_text.insert(tk.END, '~ opening gmail\n\n')
        output_text.yview(tk.END)
        webbrowser.open("https://mail.google.com")

    # opening notepad
    elif 'open notepad' in instruction:
        talk('opening notepad')
        output_text.insert(tk.END, '~ opening notepad\n\n')
        output_text.yview(tk.END)
        subprocess.Popen('notepad.exe')

    # opening command prompt
    elif 'open command prompt' in instruction:
        talk('opening command prompt')
        output_text.insert(tk.END, '~ opening command prompt\n\n')
        output_text.yview(tk.END)
        subprocess.Popen('cmd.exe')

    # opening file manager
    elif 'open file manager' in instruction:
        talk('opening file manager')
        output_text.insert(tk.END, '~ opening file manager\n\n')
        output_text.yview(tk.END)
        subprocess.Popen('explorer.exe')

    elif 'ok bye' in instruction or "bye bye" in instruction:
        talk('bye')
        output_text.insert(tk.END, '~ bye')
        output_text.yview(tk.END)

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
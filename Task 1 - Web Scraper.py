#creating a GUI based Web Scraper using tkinter, BeautifulSoup and requests
import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup

# web scraping
def scrape():
    url = url_entry.get()
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all paragraphs as an example
        paragraphs = soup.find_all('p')
        result = '\n\n'.join([p.get_text() for p in paragraphs])
        
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
        
    except requests.RequestException as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e}")

# Set up the main application window
app = tk.Tk()
app.title("Web Scraper")
app.geometry("925x500+300+200")
app.configure(bg="#7209B7")
app.resizable(False, False)

# web scraper heading
heading_label=tk.Label(app, text="WEB SCRAPER 2.0", bg="#7209B7", fg="white", font=("Ariel", 20, "bold"))
heading_label.pack(pady=5)
heading_label.place(x=20, y=20)

# slogan
slogan_label=tk.Label(app, text="Extract, Analyze, Optimize", bg="#7209B7", fg="white", font=("Ariel", 10))
slogan_label.pack(pady=5)
slogan_label.place(x=60, y=50)

# description
desc_label=tk.Label(app, text="Welcome to Web Scraper 2.0!", bg="#7209B7", fg="white", font=("Ariel", 15))
desc_label.pack(pady=5)
desc_label.place(x=55, y=160)

desc2_label=tk.Label(app, text="Here, you can extract any data \nfrom any websites", bg="#7209B7", fg="white", font=("Ariel", 15))
desc2_label.pack(pady=5)
desc2_label.place(x=50, y=240)

desc3_label=tk.Label(app, text="Scrape smarter, not harder \nGet the data you need", bg="#7209B7", fg="white", font=("Ariel", 15))
desc3_label.pack(pady=5)
desc3_label.place(x=65, y=340)

# enter URL
label_entry=tk.Label(app, text="Enter or Paste the URL here:", bg="#7209B7", fg="white", font=("Helvetica", 10))
label_entry.pack(pady=5)
label_entry.place(x=470, y=50)

# URL entry
url_entry = tk.Entry(app, width=60)
url_entry.pack(pady=5)
url_entry.place(x=470, y=80)

# Scrape button
scrape_button = tk.Button(app, text="Scrape", bg="green", fg="#ffffff", command=scrape)
scrape_button.pack(pady=5)
scrape_button.place(x=630, y=110)

# Result text area
result_text = scrolledtext.ScrolledText(app, width=60, height=20)
result_text.pack(pady=10)
result_text.place(x=400, y=150)

# Start the Tkinter event loop
app.mainloop()
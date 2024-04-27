import json
import requests
import tkinter as tk
from tkinter import simpledialog, messagebox


def champion_url_converter(champion):
    return f'https://ddragon.leagueoflegends.com/cdn/14.8.1/data/en_US/champion/{champion}.json'

def capitalize_first_letter(text):
     return text[0].upper() + text[1:]

#not implemented in functionality
def fetch_league_version(url):
    data = champion_url_converter(url)
    result = requests.get(data)
    info = result.json()

    try:
        return data['version']
    except KeyError:
        return "Unable to get version of this game"

import json

def fetch_champion_lore(champion):
    url = champion_url_converter(champion)
    result = requests.get(url)
    
    try:
        data = result.json()
        lore = data['data'][champion]['lore']
        return lore
    except (KeyError, json.decoder.JSONDecodeError):
        return "Champion lore not found or an error occurred. This champion is not created yet!"

def fetch_champion_spells(champion):
    url = champion_url_converter(champion)
    result = requests.get(url)
    
    try:
        data = result.json()
        spells = data['data'][champion]['spells']
        passive = data['data'][champion]['passive']

        spells_str = ""
        spells_str += f"{passive['name']}\n"

        for spell in spells:
            spell_name = spell['name']
            spells_str += f"{spell_name}\n"
        
        return spells_str
    except (KeyError, json.decoder.JSONDecodeError):
        return "Champion spells not found or an error occurred. This champion is not created yet!"


def get_champion_info():
    try:
        champion_prompt = simpledialog.askstring(f"Champion Info", "Please enter a champion name:")
        if not champion_prompt:  # If the user cancels the dialog
            return
        
        champion = capitalize_first_letter(champion_prompt)

        lore = fetch_champion_lore(champion)
        spells = fetch_champion_spells(champion)
        info = f"Lore:\n{lore}\n\nSpells:\n{spells}"
        messagebox.showinfo("Champion Info", info)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")





root = tk.Tk()
root.title("Champion Lore Viewer")
root.geometry('350x200')

# background_label = tk.Label(root, text="")
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(root, text=f"Get Champion info", command=get_champion_info)
button.pack(pady=20)

root.mainloop()

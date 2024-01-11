import tkinter as tk
from tkinter import * 
from tkinter.ttk import *


import json
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="ef4a3ed9335c48c6864e051a867df6d0",
    client_secret="f81d7cb1c6d8463285fc3b78ab5a5e83",
    redirect_uri="https://localhost",
    scope="user-library-read, user-modify-playback-state"))

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


root=tk.Tk()

root.geometry('1000x600')
center(root)
root.title('Spotify Control With Python')

label = tk.Label(root, text='Spotify Control With Python', font=('Gotham Circular',50))
label.pack()

icon = tk.PhotoImage(file="logo.png")
root.iconphoto(True, icon)


inputs= tk.Frame(root)
inputs.columnconfigure(0, weight=1, )
inputs.columnconfigure(1, weight=1)
inputs.columnconfigure(2, weight=1)
inputs.columnconfigure(3, weight=1)

inputtxt1 = tk.Text(inputs, height = 5, width = 20, bg = "#8DEBB0", bd=0, font=('Gotham Circular',20))
inputtxt2 = tk.Text(inputs, height = 5, width = 20, bg = "#8DEBB0", bd=0,font=('Gotham Circular',20))
inputtxt3 = tk.Text(inputs, height = 5, width = 20, bg = "#8DEBB0", bd=0, font=('Gotham Circular',20))
inputtxt1.grid(row = 0, column = 0, sticky=W+E)
inputtxt2.grid(row = 0, column = 1, sticky=W+E)
inputtxt3.grid(row = 0, column = 2, sticky=W+E)

label1 = tk.Label(inputs, text='Artist Name', font=('Gotham Circular',40))
label2 = tk.Label(inputs, text='Artist Album', font=('Gotham Circular',40))
label3 = tk.Label(inputs, text='Artist Track', font=('Gotham Circular',40))
label1.grid(row = 1, column = 0, sticky = W+E)
label2.grid(row = 1, column = 1, sticky = W+E)
label3.grid(row = 1, column = 2, sticky = W+E)

button1 = tk.Button(inputs, bg = "#B3B3B3", text='Search Albums', font=('Gotham Circular',30), command=lambda: artist_albums(inputtxt1.get('1.0',tk.END))) 
button2 = tk.Button(inputs, bg = "#B3B3B3", text='Search Tracks', font=('Gotham Circular',30), command=lambda: album_tracks(inputtxt2.get('1.0',tk.END))) 
button3 = tk.Button(inputs, bg = "#B3B3B3", text='Play Track', font=('Gotham Circular',30), command=lambda: play_song(inputtxt3.get('1.0',tk.END)))
button1.grid(row = 2, column = 0, sticky = W+E)
button2.grid(row = 2, column = 1, sticky = W+E)
button3.grid(row = 2, column = 2, sticky = W+E)

outputtxt1 = tk.Text(inputs, height = 5, width = 20, bg = "#8DEBB0", bd=0, yscrollcommand=True, font=('Gotham Circular',20))
outputtxt2 = tk.Text(inputs, height = 5, width = 20, bg = "#8DEBB0", bd=0, yscrollcommand=True, font=('Gotham Circular',20))
label4 = tk.Label(inputs, text='-Moloy & Ritik', bg='#8DEBB0', font=('Gotham Circular',30))
outputtxt1.grid(row = 3, column = 0, sticky=W+E)
outputtxt2.grid(row = 3, column = 1, sticky=W+E)
label4.grid(row = 3, column = 2, sticky=W+E)

inputs.pack(fill='x')

def artist_albums(artist):
    '''Shows the list of albums for the artist'''
    results = sp.search(q=artist, type='artist')
    artist = results['artists']['items'][0]['uri']
    results = sp.artist_albums(artist, album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    for album in albums:
        outputtxt1.insert(tk.END, album['name'])

def album_tracks(album):
    '''Lists all tracks in an album'''
    results = sp.search(q=album, type='album')
    artist = results['albums']['items'][0]['uri']
    results = sp.album_tracks(artist)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    for track in tracks:
        outputtxt1.insert(tk.END, track['name'])

def play_song(song):
    """
    put song in tkinter code e.g.
    'Light switch' is input from user
    play_song('Light switch')
    """
    results = sp.search(q=song, type='track')
    play_track = results['tracks']['items'][0]['uri']
    sp.start_playback(uris=[play_track])

webbrowser.open('open.spotify.com')

root.mainloop()



# Example codes (remove when done)
# user_info()
# album_tracks('After Laughter')
# artist_albums("Awedeo")
# play_song("The A Team")
# shuffle_on()
# shuffle_off()

# Put Tkinter initialisation code here


# Go!
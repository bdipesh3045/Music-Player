import os
import yt_dlp
from playsound import playsound
import sys
import vlc
import time
import os

# === Playlist ===

# Hello new changes added

songs_folder = os.path.join(os.getcwd(), "songs")
song_path = []

ind = 0


def clear():
    os.system("cls")


def list_song():
    print("*************************")
    print("        Song Name       ")
    print("*************************")
    # Loop through all files in the folder
    counter = 1
    for filename in os.listdir(songs_folder):
        file_path = os.path.join(songs_folder, filename)
        print(f"{counter}. {filename}")
        counter += 1


def load():
    global song_path
    if len(song_path) > 1:
        song_path = []
    for filename in os.listdir(songs_folder):
        file_path = os.path.join(songs_folder, filename)
        song_path.append(file_path)


load()
print(song_path)

# === VLC Setup ===
instance = vlc.Instance()
player = instance.media_player_new()


# === Functions ===


def play(ind):
    clear()
    media = instance.media_new(song_path[ind])
    player.set_media(media)
    player.play()
    print(f"▶️  Playing: {os.path.basename(song_path[ind])}")


def pause_song():
    clear()
    player.pause()
    print("⏸️  Paused")


def stop_song():
    clear()
    player.stop()
    print("⏹️  Stopped")


def next_song():
    clear()
    global current_index
    current_index = (ind + 1) % len(song_path)
    play(current_index)


# === Initial Load ===


# === Command Loop ===


def play_song():

    global ind
    initial = True
    while initial:
        print("Commands: 1 to play | 2 to pause | 3 to next | 4 to stop | 5 to quit")
        command = int(input(">>> "))

        if command == 1:

            list_song()
            print("Enter song no to play song:")
            ind = int(input("Enter song number:")) - 1
            play(ind)
        elif command == 2:
            pause_song()
        elif command == 3:
            next_song()
        elif command == 4:
            stop_song()
        elif command == 5:
            stop_song()
            print("👋 Exiting player.")
            initial = False
        else:
            print("Unknown command. Try again.")


def add_songs(url):

    os.makedirs(songs_folder, exist_ok=True)
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(songs_folder, "%(title)s.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "prefer_ffmpeg": True,
            "ffmpeg_location": "ffmpeg",  # Ensure ffmpeg is installed and in PATH
            "quiet": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Song downloaded and converted to mp3.")
    except Exception as e:
        print("✅ Song downloaded and converted to mp3.")
        load()


inp = 0


def msg():
    print("1 to Start Music download")
    print("2 to view songs downloaded")
    print("3 to play song")
    print("4 to quit playing song")


msg()


def main():
    loop = True
    while loop:
        clear()
        msg()
        inp = int(input("Enter the choice:"))
        clear()
        if inp == 1:

            msg()
            song_link = input("Enter the song link:")
            add_songs(song_link)

        elif inp == 2:
            clear()
            msg()
            list_song()

        elif inp == 3:
            clear()

            # number = int(input("Enter the song number from above:"))
            play_song()

        elif inp == 4:

            print("Program being stopped")
            loop = False
        else:
            clear()
            msg()
            print("Invalid command")


main()

# shite-music-player
A ~~low quality, pish~~ *streamlined and non resource-intensive* music player written in Python.

 **Features**

* Support for opening a specific file or an entire folder 
* Random shuffling of tracks
* ~~badly made~~ simple, intuitive UI
* No AI slop^1






^1  All slop is 100% human made.
**How it works**

When the 'Open File' option is selected, the program will ask for a single file and play it. I know, mind-blowing stuff. I'm totally not padding out this document so it seems more impressive.

When the 'Open Folder' option is picked, the program asks you for a directory, and scans it (and one layer of sub-folders, to allow for playlists) for audio files. It then shuffles them randomly until there is none left. Scanning of sub-folders can be turned off.

To skip a song, you can press the right arrow while the window is selected. Similarily, press SPACE to pause/unpause. There is no support at present for rewinding a song.

**Requirements**

You need both Python and Pygame installed on your computer. (I could make an actual distribution that includes these but I cba. It's harder than it sounds, pyinstaller is janky.)

To install:

Install the latest version of Python from [https://www.python.org/downloads/](https://www.youtube.com/watch?v=dQw4w9WgXcQ). 

Follow the installation process. Once installed, open CMD (Windows) / Terminal (Mac) / \<whatever the Linux shell is called\> (be honest, you dont need this guide if you're using Linux) and run the following command: `python3 -m pip install pygame`

Once pygame is installed, you can close the window and the script should run as normal.

NB: .py files will by default open in IDLE (Python's code editor) rather than running immediately.

You also need actual music files (.mp3 or .wav). There are many (100%, totally legal fr) sites you can obtain these from which I will not list as I don't want to get in trouble.

**Why not just use Spotify?**

* No ads
* Unlimited skips
* Random shuffle ([Spotify's shuffle mode is not truly random](https://www.slashgear.com/1546972/how-to-fix-spotify-shuffle-feature/))
* Made by a random person (this is 100% a positive)
* ~~In the event of nuclear war and the destruction of the Internet, you can still listen to music with this~~
* Steven flowe
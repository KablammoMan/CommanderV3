# CommanderV3
Like CommanderV2 (works anywhere) but with Deta Space (better hosting).

# Imports
Client:
- deta
- socket
- mouse
- screeninfo
- random
- keyboard
- subprocess
- threading
- webbrowser
- sys

Master:
- deta

# How to Use
1. Replace `config.api_key` on line 48 of `client.py` with your Deta Project key
2. Convert `client.py` to exe using preferred tool (I recommend PyInstaller)
3. Run the new `.exe` file on the target's computer
4. Run `admin.py` and manage all your clients
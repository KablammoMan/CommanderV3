# CommanderV3
Like CommanderV2 (works anywhere) but with Deta Space (better hosting).

# Imports
Client:
- deta
- keyboard
- mouse
- os
- random
- screeninfo
- shutil
- socket
- subprocess
- sys
- threading
- webbrowser

Master:
- deta
- os
- time

# How to Use
1. Replace `config.api_key` on line 48 of `client.py` and line 6 of `admin.py` with your Deta Project key
2. Convert `client.py` to `.exe` using preferred tool (I recommend PyInstaller)
3. Run the new `.exe` file on the target's computer
4. Run `admin.py` and manage all your clients
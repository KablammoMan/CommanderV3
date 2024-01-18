# CommanderV3
Like CommanderV2 (works anywhere) but with Deta Space (better hosting).

# End User License Agreement
By using the software provided you automatically agree to the following EULA:
1. I (KablammoMan) am not responsible for any trouble that you get in (legal, institutional, etc...) for using the software provided, however, if I am caught using it I will accept responsibility for my actions and take whatever punishment is deemed appropriate.
2. The software is provided as is and I make no guarantees of the software working on all computers at all points in time.

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
1. Replace `config.api_key` on line 69 of `client.py` and line 7 of `admin.py` with your Deta Project key
2. Convert `client.py` to `.exe` using preferred tool (I recommend PyInstaller)
3. Run the new `.exe` file on the target's computer
4. Run `admin.py` and manage all your clients

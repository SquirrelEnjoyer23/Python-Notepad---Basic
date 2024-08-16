print("""
__________          __  .__                     _______          __                           .___
\______   \___.__._/  |_|  |__   ____   ____    \      \   _____/  |_  ____ ___________     __| _/
 |     ___<   |  |\   __\  |  \ /  _ \ /    \   /   |   \ /  _ \   __\/ __ \\____ \__  \   / __ | 
 |    |    \___  | |  | |   Y  (  <_> )   |  \ /    |    (  <_> )  | \  ___/|  |_> > __ \_/ /_/ | 
 |____|    / ____| |__| |___|  /\____/|___|  / \____|__  /\____/|__|  \___  >   __(____  /\____ | 
           \/                \/            \/          \/                 \/|__|       \/      \/ 
""")
print("WARNING! All notes are cleared when window is closed WARNING!")
print("""use the command "view" to see your notes""")
print("""use the command "create YourNoteHere" to Make a note""")
Saved_Notes = []

def ReadNotes():
    for Note in Saved_Notes:
        print(Note)



def BeginMain():
    User_Input = input().split(" ",1)
    ViewCommand = "view"
    CreateCommand = "create"
    if User_Input[0] == ViewCommand:
        print("viewed")
        BeginMain()

    if User_Input[0] == CreateCommand:
        print("viewed")
        Saved_Notes.append(User_Input[1]+"\n")
        ReadNotes()
        #print(Saved_Notes)
        BeginMain()

BeginMain()
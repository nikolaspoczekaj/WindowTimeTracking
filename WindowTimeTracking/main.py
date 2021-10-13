import win32gui
import re
import time
import os
import json


### TURN ONLY SECONDS INTO READABLE TIME ###
def int_in_time(secs):
    string = ""
    hours = 0
    minutes = 0
    seconds = 0
    while secs >= 3600:
        hours += 1
        secs -= 3600
    while secs >= 60:
        minutes += 1
        secs -= 60
    seconds = secs
    if hours > 0:
        string = string + f"{hours}h "
    if minutes > 0:
        string = string + f"{minutes}m "
    string = string + f"{seconds}s "
    return string


### TRIM SECONDS OUT OF JSON TEXT ###
def trimmed(string):
    trim = string
    trim = trim.replace("[{'time': ", "")
    trim = trim.replace("}]", "")
    return trim

### FILENAME ###
filename = 'data.txt'


### REFRESHRATE IN SECONDS ###
refreshrate = 5


### TIME VARIABLES ###
vsCodeTime = 0
spotifyTime = 0
iuLearnTime = 0
youtubeTime = 0
eclipseTime = 0
outlookTime = 0
stackOverflowTime = 0
otherTime = 0



### READ OLD FILE ###
data = {}
try:
    with open(filename) as json_file:
        data = json.load(json_file)

    vsCodeTime = int(trimmed(str(data['VsCode'])))
    spotifyTime = int(trimmed(str(data['Spotify'])))
    iuLearnTime = int(trimmed(str(data['IU Learn'])))
    youtubeTime = int(trimmed(str(data['YouTube'])))
    eclipseTime = int(trimmed(str(data['Eclipse'])))
    outlookTime = int(trimmed(str(data['Outlook'])))
    stackOverflowTime = int(trimmed(str(data['Stack Overflow'])))
    otherTime = int(trimmed(str(data['Other'])))    
except:
    print()

print(f"Starting in {refreshrate} Seconds...")

### TRACK ACTIVE WINDOW AND ADD TIME ###
while True:
    
    time.sleep(refreshrate)
    os.system('cls||clear')
    from win32gui import GetWindowText, GetForegroundWindow
    window = GetWindowText(GetForegroundWindow())
    ### PRINT ACTIVE WINDOW ###
    print("Active Window: " + window)

    if window.find("Visual Studio Code") != -1:
        vsCodeTime += refreshrate
    elif window.find("Spotify") != -1:
        spotifyTime += refreshrate
    elif window.find("IU Learn") != -1:
        iuLearnTime += refreshrate
    elif window.find("YouTube") != -1:
        youtubeTime += refreshrate
    elif window.find("Eclipse") != -1:
        eclipseTime += refreshrate
    elif window.find("Outlook") != -1:
        outlookTime += refreshrate
    elif window.find("Stack Overflow") != -1:
        stackOverflowTime += refreshrate
    else:
        otherTime += refreshrate


    ### PRINT CURRENT TIMES ###
    print("VSCode: " + int_in_time(vsCodeTime))
    print("Spotify: " + int_in_time(spotifyTime))
    print("IU Learn: " + int_in_time(iuLearnTime))
    print("YouTube: " + int_in_time(youtubeTime))
    print("Eclipse: " + int_in_time(eclipseTime))
    print("Outlook: " + int_in_time(outlookTime))
    print("Stack Overflow: " + int_in_time(stackOverflowTime))
    print("Other: " + int_in_time(otherTime))
    
    
    
    
    ### DELETE OLD FILE ###
    try:
        os.remove(filename)
    except:
        print()


   
   
    ### CREATE NEW FILE ###
    data = {}
    data['VsCode'] = []
    data['Spotify'] = []
    data['IU Learn'] = []
    data['YouTube'] = []
    data['Eclipse'] = []
    data['Outlook'] = []
    data['Stack Overflow'] = []
    data['Other'] = []
    data['VsCode'].append({
        'time': vsCodeTime
    })
    data['Spotify'].append({
        'time': spotifyTime
    })
    data['IU Learn'].append({
        'time': iuLearnTime
        })
    data['YouTube'].append({
        'time': youtubeTime
        })
    data['Eclipse'].append({
        'time': eclipseTime
        })
    data['Outlook'].append({
        'time': outlookTime
        })
    data['Stack Overflow'].append({
        'time': stackOverflowTime
        })
    data['Other'].append({
        'time': otherTime
        })
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent = 4)


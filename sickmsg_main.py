import pywhatkit
from datetime import datetime
from datetime import date
import time


med_dict = {
    'anarex': "Taken anarex.", 
    'imodium': "Taken imodium", 
    'panadol': "Taken panadol", 
    'probiotic': "Taken lacteofort",
    'antibiotics': "Taken antibiotics"
}

mins = datetime.now().minute
MINS_CHECK = 4
n = datetime.now().hour

if mins > MINS_CHECK:
    n += 1

while True:
    pywhatkit.sendwhatmsg('+6596562765', 'Check your temperature!', n, MINS_CHECK)
    curr_temp = input("Current temperature: ")
    has_meds = input("Did you take medication? [y|n]: ")
    
    meds = ''
    while has_meds == 'y':
        type_meds = input("What meds did you take?: [anarex, imodium, panadol, probiotic, antibiotics]: ")
        meds += med_dict[type_meds] + ' '
        has_meds = input("Did you other medication? [y|n]: ")
    
    req = input("Anything you want to report?: ")

    time = datetime.now().strftime("%H:%M")
    today = date.today()
    pywhatkit.sendwhatmsg('+6596417371', f"{today} {time}: Achi's temperature is {curr_temp}°C. {meds}| Help needed: {req}", n, MINS_CHECK + 2)
    
    with open("sick_log.txt", 'w') as output_file:
        

    n += 1


import pywhatkit
from datetime import datetime
from datetime import date
import time

YOUR_PHONE_NUMBER = 0
RECIPIENT_GROUP_LINK = 1 
YOUR_NAME = ''

med_dict = {
    'anarex': "Taken anarex.", 
    'imodium': "Taken imodium", 
    'panadol': "Taken panadol", 
    'probiotic': "Taken lacteofort",
    'antibiotics': "Taken antibiotics",
    'nurofen': "Taken nurofen"
}

mins = datetime.now().minute
MINS_CHECK = 27     # I choose random timestamps and XX:27 just vibes with me
n = datetime.now().hour

if mins > MINS_CHECK:
    n += 1

while True:
    pywhatkit.sendwhatmsg(YOUR_PHONE_NUMBER, 'Check your temperature!', n, MINS_CHECK)
    curr_temp = input("Current temperature: ")
    oxy = input("Oximeter reading (%): ")
    has_meds = input("Did you take medication? [y|n]: ")
    
    meds = ''
    while has_meds == 'y':
        type_meds = input("What meds did you take?: [anarex, imodium, panadol, probiotic, antibiotics]: ")
        if type_meds in meds:
            meds += med_dict[type_meds] + ' '
        else:
            meds += f"Taken {type_meds}. "
        has_meds = input("Did you other medication? [y|n]: ")
    
    req = input("Anything you want to report?: ")
    if not req:
        req = "None"

    curr_time = datetime.now().strftime("%H:%M")
    today = date.today()
    mins = datetime.now().minute
    pywhatkit.sendwhatmsg_to_group(RECIPIENT_GROUP_LINK, f"{today} {curr_time}: {YOUR_NAME}'s temperature is {curr_temp}°C. Oximeter: {oxy}%. {meds}| Remarks: {req}", n, mins + 1)
    
    print("** Update sent **")
    n += 1
    time.sleep(3250)


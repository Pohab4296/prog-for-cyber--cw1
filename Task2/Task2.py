# Security Event Logger- Task2


import random
from datetime import datetime

#  predfinded credentials 
correctuser = "B00156015" #oredefined username
correctpassword= "letmein" # predefinded password
ip = "192.168.1.25"   # predefined ip address
logged_in = False # status of login.

# Keep asking until the correct username and password are entered
while not logged_in: # continues while you aren't logged in
    username = input("Pleasse enter your Username: ") # takes the users input for username and stores it in the username variable
    password = input("Please enter your Password: ") # takes the users input for password and stores it in the password variable

    # Generate event details for this attempt
    event_id = random.randint(1000, 9999) # generates a random number to act as event id. Used the random function that was imported
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S") # uses the date and time to act as the timestamp, stored in the timestamp variable. Uses the datatime function imported

    # Check the credentials
    if username == correctuser and password == correctpassword: # checks the user entered details against the predefined values
        event = "Successful login" # changes event to successful login
        logged_in = True # changes status to logged in
    else:
        event = "Failed login" # if incorrect changes event to failed login

    # Print the event log for this attempt
    print("----Security Event Log ---")   #title
    print("Event ID:", event_id)            # ID for the event
    print("Username:", username)            # username of the event 
    print("IP Address:",ip)                 # IP address concerned
    print("Event:", event)                  # The event that caused the incident
    print("Timestamp:", timestamp)           #the time it took place
    print("----------------------")

print("Access granted.")
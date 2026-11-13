# Security Incident Manager using Dictionaries

# 1. Create a dictionary containing username, IP address, event type and risk level
incident = {
    "username": "B00156015",
    "ip_address": "192.168.8.8",
    "event_type": "Suspusious Activity",
    "risk_level": "None"
}

# 2. Display the username and IP address
print("--- Incident Details ---")               # displays title
print("Username:", incident["username"])        # displays username
print("IP Address:", incident["ip_address"])    # dislpys Ip address

# 3. Add a new field called status
incident["status"] = "Under Investigation"      # adds a status to the vent
print("\nNew field 'status' added.")            # print an output to inform the user

# 4. Update the risk level
incident["risk_level"] = "High"                             # adds a risk level to the event
print("Risk level updated to:", incident["risk_level"])     # print an update to the user increasing the risk level

# 5. Remove one field from the dictionary (event type)
try:                                                                # start of error handling
    del incident["event_type"]                                      # deletes the event type of the dictionary
    print("Field 'event_type' removed.")                            # print an update to the user
except KeyError:                                                    # uses Exception handling if there is nothing in the event_type field
    print("Field 'event_type' not found, nothing was removed.")     # print an update to the user
        
# 6. Display all remaining keys and values
print("\n--- Remaining Incident Data ---")                          # prints a title to the user
for key, value in incident.items():                                 # loops for all the key values in the incident dictionary
    print(key + ":", value)                                         # outputs the content of the key and the value together with an : between the two

# 7. Display the total number of key-value pairs
print("\nTotal number of key-value pairs:", len(incident))          #prints an output to the user along with the length of the incident dictionary

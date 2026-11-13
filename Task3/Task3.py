#Task 3: IP Address Validator (using Function)
# IP Address Validator

def validate_ip(ip):
    # Remove unnecessary spaces
    ip = ip.strip()

    # Check whether the IP address contains any dots
    if "." not in ip:
        return False

    # Check for exactly three dots
        return False

    # Split into parts and check there are 4 groups of numbers
    parts = ip.split(".") #Spliting the address on the dots
    if len(parts) != 4:
        return False

    # Check each part is a number between 0 and 255
    for part in parts:
        if not part.isdigit():   # rejects letters, empty parts, negatives
            return False
        number = int(part) #ensures only whole positive numbers are entered
        if number < 0 or number > 255: #ensures the number entered are between 0 and 255
            return False
        
    # if any option of the function returns False then the address is invalid.

    return True # if all are true then the function returns valid.


# Main program And IP input
ip = input("Enter an IP address: ") #accepts the input of an up address and stores it in the IP variable

if validate_ip(ip): #runs the ip variable through the validate ip function
    print("Valid IP address")
else:
    print("Invalid IP address")

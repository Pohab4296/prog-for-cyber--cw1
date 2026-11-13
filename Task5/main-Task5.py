import security_tools

# Ask the user to enter a password and IP address
password = input("Enter your password: ")
ip_addr = input("Enter an IP address: ")

# Validate the password
if security_tools.validate_password(password):
    print("Password is valid.")
else:
    print("Password is not strong enough.")
    print("Suggested strong password:",
 security_tools.generate_password())

# Validate the IP address
if security_tools.validate_ip(ip_addr):
    print("IP address format is valid.")
else:
    print("IP address format is invalid.")

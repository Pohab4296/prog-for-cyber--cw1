# Basic Security Tool - Task01
import sys
# Local Variables 
correctuser = "paul" # the valid login Username
correctpassword = "P@$$w0rd" # the valid login and the main menu Password
COUNTERpass= "counterpaul"   # Op1-SecurityEventPassword

maxLOGINattempt = 3     # Maximum Login Attempts
totalAttempts = 10      # Maximum Attempts Permitted

# Startup authentication
print("=== Authentication Required ===")
failed = 0 # Zeros the number of attempts

while True:  # Once authentication is successful
    username = input("Username: ") # takes the username as an input and stores it in the username variable
    password = input("Password: ") # takes the password as an input and stores it in the password variable

    if username == correctuser and password == correctpassword: # determines if the username and password match the store values
        print("Authentication successful.\n") # prints acceptance if correct
        break

    failed += 1 #adds one to the failed counter if unsuccessful
    print("Authentication failed. Attempt", failed, "of", maxLOGINattempt, "\n") # prints a message to say unsuccessful on attempt

    if failed >= maxLOGINattempt: # once failed attempts reaches the maximum number of allowed attempts
        print("Account frozen for 24 hours.") # prints a message that the account if frozen
        sys.exit()

#  Main menu     
while True:  # loops menu until option 4 picked
    print("\n===== SECURITY MENU =====")
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")

    try: # start of error handling
        # takes the user's menu choice and converts it to a whole number
        choice = int(input("Select an option (1,2,3,4): ")) # takes the users input and stores it in the choice variable
    except ValueError: # exception handling start
        # runs if the input is letters, symbols, spaces or empty
        print("Invalid input. Please enter a number (1-4), not text or symbols.") # error message notification 
        continue  # go back to the top and show the menu again
    except KeyboardInterrupt:
        # runs if the user presses Ctrl+C
        print("\nProgram interrupted. Exiting.")
        break
    except EOFError:
        # runs if the input stream ends unexpectedly
        print("\nNo input received. Exiting.")
        break

    # ----- 1. Security Event Counter -----
    if choice == 1:
        print("--- Security Event Counter ---")
        correct = 0    # Variables for corrects guesses,  setting counter to 0
        incorrect = 0  # Variables for incorrect guesses, setting counter to 0
        count = 0      # Variables for counting attempts setting counter to 0

        while count < totalAttempts:  # while the attempt is below the total number of attempts allowed
            guess = input("Enter password (" + str(count + 1) + "/" + str(totalAttempts) + "): ")  # takes the attempt from the user
            if guess == COUNTERpass:  # compares the attempt against the set password
                correct += 1          # if correct adds one to the correct counter
            else:
                incorrect += 1        # if not adds one to the incorrect counter
            count += 1                # increase the counter by 1

        percent_incorrect = (incorrect / totalAttempts) * 100  # calculates the incorrect number against the total as a percentage

        print("\nCorrect passwords:", correct)      # displays the number correct
        print("Incorrect passwords:", incorrect)    # displays the number incorrect
        print("Incorrect percentage:", round(percent_incorrect, 1), "%")  # displays the % incorrect rounded to 1 decimal place

        if percent_incorrect > 50:  # criteria for whether an alert is raised, in this case more than 50% wrong
            print("ALERT: More than 50% of password attempts were incorrect!")  # displays the alert message

    # ----- 2. Brute-Force Simulation -----
    elif choice == 2:
        print("\n--- Brute-Force Simulation ---")
        BRUTEpass = "brutepaul"   # brute-force Password
        attempts = 0          # zeroes the attempts counter
        cracked = False       # sets cracked status
        MaxBRUTEattempts = 5  # maximum brute-force attempts

        while attempts < MaxBRUTEattempts and not cracked:  # loop while attempts remain and the password is not cracked
            guess = input("Guess the password (attempt " + str(attempts + 1) + "/" + str(MaxBRUTEattempts) + "): ")  # takes the guess from the user
            attempts += 1  # increases the counter by 1

            if guess == BRUTEpass:  # compares the guess to the stored value
                cracked = True      # if the guess is correct the value becomes True

        if cracked:  # once cracked displays how many attempts it took
            print("Password cracked in", attempts, "attempt(s).")
        else:
            print("Maximum attempts (" + str(MaxBRUTEattempts) + ") reached. Password not cracked.")  # message that the password was not cracked

    # ----- 3. Login Authentication -----
    elif choice == 3:
        print("\n--- Login Authentication ---")
        login_failed = 0  # zeroes the counter for failed login attempts

        while True:  # keeps asking until success or too many failures
            username = input("Username: ")  # takes the user's input for the username
            password = input("Password: ")  # takes the user's input for the password

            if username == correctuser and password == correctpassword:  # compares the entered values against the stored variables
                print("Authentication succeeded.")  # success message
                break  # leaves the login loop and returns to the menu

            login_failed += 1  # adds one to the failed counter
            print("Authentication failed. (" + str(login_failed) + "/" + str(maxLOGINattempt) + ")")  # shows the failed attempt number

            if login_failed >= maxLOGINattempt:  # compares the failures against the maximum permitted
                print("Account frozen for 24 hours.")  # displays the frozen account message
                break  # leaves the login loop and returns to the menu

    # ----- 4. Exit -----
    elif choice == 4:
        print("Thank you for using the security tool")  # displays a thank you message
        break  # leaves the menu loop, ending the program

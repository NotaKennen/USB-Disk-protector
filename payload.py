import time

passwordStorage = "password.txt" # location where the password is stored at, same as the payload.py password storage
                     # input the whole path, including the file name

password = "password" # If they input this password, the program will not run.
# todo: store the password more securely than this, idk any cryptography

timelimit = 300 # How much time do they have until the script executes (unless the password is correct) (seconds)
timelimit += time.time() # setting the time limit to epoch (dont touch)

try:
    while time.time() < timelimit:
        with open(passwordStorage, "r") as file:
            answer = file.read()
        if str(answer) == str(password):
            quit()
        else:
            time.sleep(10)
except Exception as e:
    pass
    

# Put your code here (or a function which runs a script or something)
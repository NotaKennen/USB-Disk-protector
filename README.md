## MemWare USB Disk protector
Traps your USB Disk so that your files can stay (partially) safe.

Putting this onto your USB disk means that once plugged onto a computer, it will ask for a password. If the password is incorrect, it will run (usually malicious) programs to teach the intruder a lesson. If the password is correct, you can browse your files just fine. 

The protector will create a small TXT file onto your system, and if deleted (or the password changed) it will absolutely smash your computer (depending on the script that you placed into it). I'm planning on adding a "trusted computers" section that will just completely ignore certain computers based on name.

### Setup
1. Set up your code on the Payload.py
2. Configure settings in both .py files
3. Compile the .py files
4. Put it all on your USB Disk
5. Have fun

Theoretically you could remove the time limit to make the USB disk a makeshift ducky.

### Possible issues
- The code is really unstable because the files arent linked to each other very well, expect issues with that.
- The program only works with AutoRun compatible windows machines...
- All the paths and passwords are stored in simple strings, even a basic reverse-engineering technique will break the entire system (fixable with basic obfuscation).

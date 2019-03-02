import datetime
import subprocess
import sys

# Change the name of your friend here
friend = sys.argv[1]

# Change the message here
message = sys.argv[2]

# Change the time of sending message here
try:
    time = sys.argv[3]
except IndexError:
    time = "now + 1 min"

with open("pyzapp.log", "a") as f:
    command = 'echo "export DISPLAY=:0 && python whatsapp.py \'{}\' \'{}\'" | at {}'.format(friend, message, time)
    # Write the command and datetime to the log file for keeping track
    f.write("{}\n{}\n\n".format(datetime.datetime.now().isoformat(), command))
    # Call the command
    subprocess.call(command, stdout=f, stderr=f, shell=True)


# Usage: python pyzapp.py "Tanmoy" "Banchod leura saala"

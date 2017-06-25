import argparse
import re
import datetime
import subprocess

from whatsapp import PyWhatsApp

class ValidationError(Exception):
    """Raise when the time argument does not match the format"""

class FutureError(Exception):
    """Raise when the time argument is not in future"""

# This is the default message. Change it to change the default message being sent by Pyzapp
message = "'I am sending this message via Python Code. You want to try??!!'"

# This is the default time for sending message, if time is not provided
time = "now + 1 min"


def dateValidator(string):
    try:
        if not re.search(r'\d{2}:\d{2}\s\d{2}\.\d{2}\.\d{4}', string):
            raise ValidationError
        hour,minute, day, month, year = map(int, re.findall(r'\d{2,4}', string))
        scheduled_time = date = datetime.datetime(hour=hour, minute=minute, day=day, month=month, year=year)
        if scheduled_time < datetime.datetime.now():
            raise FutureError
    except (ValueError, TypeError, ValidationError):
        print("Invalid Date Format: Please use the mentioned format. \nType python pyzapp.py --help for more information")
        exit(1)
    except FutureError:
        print("Time Set in Past: You cannot schedule a message to be sent in past. \nPlease enter a valid date in future")
        exit(1)

    return True

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("friend", help="Write the name of your friend as shown on ur WhatsApp Chat Screen")
    parser.add_argument("-m", "--message", help="Message to send to your friend within double quotes. \
                                        Default is \"I am sending this message via Python Code. \
                                        You want to try??!!\"")
    parser.add_argument("-t", "--time", help="Date and time when u want to send your message. \
                                        Enter in the format \"HH:MM DD.MM.YYYY\". Default is 12 AM of next day")
    args = parser.parse_args()

    global friend
    friend = "'" + args.friend + "'"

    if args.message:
        global message
        message = "'" + str(args.message) + "'"
    if args.time and dateValidator(args.time):
        global time
        time = str(args.time)

    f = open("pyzapp.log", "a")
    command = 'echo "export DISPLAY=:0 && python whatsapp.py ' + friend + ' ' + message + '" | at ' + time
    f.write(datetime.datetime.now().isoformat())
    f.write("\n")
    f.write(command)
    subprocess.call(command, stdout=f, stderr=f, shell=True)
    f.write("\n\n")
    f.close()

if __name__ == "__main__":
    main()

from py_imessage import imessage
import time

#Enter the phone number of the recepient below
phone = ""

# if not imessage.check_compatibility(phone):
#     print("Not an iPhone")

#Open and read the songlyrics textfile
with open("songlyrics", "r") as fh:
    all_lines = fh.readlines()
txtLen = len(all_lines)

for x in range(txtLen):
    time.sleep(1)
    guid = imessage.send(phone, str(all_lines[x]))#Actual sending of messages


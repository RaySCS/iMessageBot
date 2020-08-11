# iMessageBot
Have you seen the viral trend on Tik Tok regarding people sending music lyrics to their friends? Well I decided to code it up with Python! 


# How to Run

## Prerequisites

Install Python3

Install Pip and virtualenv

Install Pipenv

## Edits to Script
* <b>In the imessage.py</b>, change the empty phone variable to the phone number where you would like the lyrics to be delivered.
* <b>In the songlyrics text file</b>, change text to the lyrics of song (copy+paste from Google).

Voila, and there you go! Remember, this script will only run with Macs configured with iMessage Apple ID.


### Troubleshooting
<b>Getting an SQLite Operational Error?</b>
<br>
Give terminal "full disk access" on Mac for py-imessage to work: 
System Preferences -> Security & Privacy -> Privacy -> Full Disk Access -> + -> Click Terminal
You'll receive this error once you run the final script if you don't: 
sqlite3.OperationalError: unable to open database file

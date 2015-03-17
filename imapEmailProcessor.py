"""This little script removes IMAP related stuff from emails.
This includes those pesky =20 and similar.

Usage:
Change the raw_email_file_name to the text file your email is contained in

Janis Lesinskis - March 2015
"""

import quopri
raw_email_file_name = 'shuttleWarmupMarch2015.txt'
raw_email = open(raw_email_file_name, 'r')
output_file = open('converted' + raw_email_file_name, 'w')
quopri.decode(raw_email, output_file)

"""This little script processes out quoted-printable formatting for emails
that you might encounter when viewing raw emails on the server.
This includes those pesky =20 and similar.

Usage:
Change the raw_email_file_name to the text file your email is contained in

Janis Lesinskis - March 2015
"""

import quopri
raw_email_file_name = 'rawEmailMarch2015.txt'
with open(raw_email_file_name, 'r') as raw_email:
    with open('converted' + raw_email_file_name, 'w') as output_file:
        quopri.decode(raw_email, output_file)

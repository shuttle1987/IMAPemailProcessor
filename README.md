# IMAP email processor
Sometimes when you are looking over the raw source for emails you will find extra formatting.
Email clients will do this processing for you and you will generally speaking see the text as it was sent to you.

If the email is encoded with http://en.wikipedia.org/wiki/Quoted-printable you might see extra "=" characters all over your emails.

This script uses the Python standard library to process the escaped characters and give you the plain text output.

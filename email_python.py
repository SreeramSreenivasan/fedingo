#! /usr/bin/python 
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test HTML Email"
msg['From'] = sender
msg['To'] = receiver

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link for activation:\nhttp://example2.com"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://example2.com">link</a> you wanted.
       <img src="http://example2.com/static/hello.jpg"/>
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html. 
part1 = MIMEText(text, 'plain') 
part2 = MIMEText(html, 'html')

# Attach parts into message container.  
msg.attach(part1) 
msg.attach(part2) 

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(sender, receiver, msg.as_string())
s.quit()

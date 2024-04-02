import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "ramiro.carnicer@tarmac.io"
password = "nhta rqly hzns bnwr"

receiver = "ramiro.carnicer@tarmac.io"
context = ssl.create_default_context()

message = """\
Subject: HI!
HELLO!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["From"] = "Simeon Markov"
message["To"] = "testuser1273@outlook.com"
message["Subject"] = "test subject"
body = template.substitute({"name": "Jonh"})
message.attach(MIMEText(body, "html"))

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser1273@outlook.com", "GreenGarden147@")
    smtp.send_message(message)
    print("Message sent")
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["From"] = "Simeon Markov"
message["To"] = "testuser1273@outlook.com"
message["Subject"] = "test subject"
message.attach(MIMEText("test text", "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser1273@outlook.com", "GreenGarden147@")
    smtp.send_message(message)
    print("Message sent")
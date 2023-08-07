import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import web

def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        # Creation of the email itself
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = receiver_email
        email_message['Subject'] = subject

        # the message the email holds
        email_message.attach(MIMEText(message, 'plain'))

        # SMTP server connection and sending email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, email_message.as_string())
        
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Usage example
if __name__ == "__main__":
    sender_email = 'david.chinchilla@uconn.edu'  
    sender_password = 'Pclover12' 
    receiver_email = 'david.chinchilla@uconn.edu'  #
    subject = 'Meals for today'
    message = 'Hello, this is a test email sent with Python!'

    send_email(sender_email, sender_password, receiver_email, subject, message)
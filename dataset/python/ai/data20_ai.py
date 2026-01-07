import smtplib
import ssl

class AI_EmailSender:
    def __init__(self, sender_email, receiver_email, subject, body):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.subject = subject
        self.body = body
        self.full_message = self._compose_message()
        self.smtp_server = "smtp.gmail.com"
        self.port = 465  # SSL port for Gmail

    def _compose_message(self):
        # Construct full email with subject header
        return f"Subject: {self.subject}\n\n{self.body}"

    def send_email(self, password):
        # Create SSL context for secure connection
        ssl_context = ssl.create_default_context()
        
        # Connect to Gmail SMTP server using SSL
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=ssl_context) as server:
            print(f"Connecting to SMTP server {self.smtp_server} on port {self.port}...")
            
            # Login using provided credentials
            server.login(self.sender_email, password)
            print(f"Successfully logged in as {self.sender_email}")
            
            # Send the email
            server.sendmail(self.sender_email, self.receiver_email, self.full_message)
            print(f"Email successfully sent to {self.receiver_email}")

if __name__ == "__main__":
    # User-defined inputs
    sender = "automationtest3798@gmail.com"
    receiver = "dixit.2@iitj.ac.in"
    subject_text = "Hi there"
    body_text = "This message is sent from Python."
    
    email_sender = AI_EmailSender(sender, receiver, subject_text, body_text)
    
    # Prompt user for password
    user_password = input("Type your email password and press enter: ")
    
    # Send the email
    email_sender.send_email(user_password)

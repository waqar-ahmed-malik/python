import smtplib
from os.path import basename
import email.mime.multipart
import email.mime.text
import email.mime.application


class SMTPEmailModule:
    def __init__(self, sender_email: str, sender_password: str):
        self.server = smtplib.SMTP('smtp.gmail.com:587')  
        self.sender_email = sender_email
        self.server.starttls()  
        self.server.login(self.sender_email , sender_password)

    def __del__(self): 
        self.server.quit()


    def send_email(self, msg_text: str, subject: str, receiver_email: str, msg_id: str=None, file_data: bytes = None,file_name: str = None):
            msg = email.mime.multipart.MIMEMultipart()
            msg['from'] = self.sender_email
            msg['to'] = receiver_email
            if msg_id:
                msg['in-reply-to'] = msg_id
                msg['subject'] = "Re: " + subject
                msg['references'] = msg_id
                msg.add_header('reply-to', receiver_email)
            else:
                msg['subject'] = subject
            text_part = email.mime.text.MIMEText(msg_text, "plain")
            msg.attach(text_part)
            # Attach a file
            if file_name:
                attach_part = email.mime.application.MIMEApplication(file_data, Name=basename(file_name))
                attach_part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_name)
                msg.attach(attach_part)
            self.server.sendmail(msg['from'], [msg['to']], msg.as_string())

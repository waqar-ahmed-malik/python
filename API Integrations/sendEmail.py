import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


MailBody = "Hi Team, <br> <br>  Please find below the status report for TIME Job <br><br>  <head>  <meta http-equiv=""Content-Type"" content=""text/html; charset=utf-8"">  <title>html title</title>  <style type=""text/css"" media=""screen"">    table{    border: 1px solid black;    background-color: #DCDCDC;        empty-cells:hide;    }    td.cell{     border: 1px solid black;   background-color: white;    }  </style></head><body>  <table style=""border: blue 1px solid;""><tr> <th>PROJECT_NAME</th>   <th>JOB_NAME</th>     <th>COMPONENT_NAME</th>    <th>COMPLETED_AT</th> <th>STATUS</th> <th>MESSAGE</th></tr>"
MailSubject = "Job Status"
MailPreamble = """Your mail reader does not support the report format.!"""
    
def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our html email""" 
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = MailSubject
    MESSAGE.preamble = MailPreamble
    HTML_BODY = MIMEText(BODY, 'html')
    MESSAGE.attach(HTML_BODY)
    server = smtplib.SMTP('smtp.gmail.com:587')
    if __name__ == "__main__":
        server.set_debuglevel(1)
        password = "mypassword"
        server.starttls()
        server.login("iris.iv.notifications@gmail.com","InstantView21!")
        server.sendmail(FROM, [TO], MESSAGE.as_string())
        server.quit()
    if __name__ == "__main__":
        TO = "waqar.ahmed@polestarllp.com"
        FROM ='iris.iv.notifications@gmail.com'
        py_mail("Test email subject", MailBody, TO, FROM)
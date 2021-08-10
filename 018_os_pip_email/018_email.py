import smtplib
from email.message import EmailMessage

smpt = smptlib.SMTP_SSL('smtp.zone.eu', 465)
smpt.login('python@mrartful.com', 'dsf342asda')

msg = EmailMessage()
msg['Subject'] = 'Test mail written by python'
msg['From'] = 'python@mrartful.com'
msg['To'] = 'roman.kutselepa@gmail.com'
msg.set_content('This is a sample email that was created and sent by python script')
msg.add_alternative("""
<h1> Hello World </h1>
<p style="color:red">
This is a sample email that was created by python script
</p>
""", subtype='html')

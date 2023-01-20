import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Oluwaseun Aji'
email['to'] = 'seunajifolokun@gmail.com'
email['subject'] = 'You won a jackport'

email.set_content('I am learning a new skill!!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ajifolokunoluwaseun83@gmail.com', 'Nokialomo@1')
    smtp.send_message(email)

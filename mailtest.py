import smtplib
from email.mime.text import MIMEText

def mailTest():
    msg = MIMEText('This is a test mail from python.')
    msg['Subject'] = 'Python Mail Test'
    msg['From'] = 'consult.saurabh@gmail.com'
    msg['To'] = 'consult.saurabh@gmail.com'

    try:
        print('1')
        s = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)
        print('2')
        s.ehlo()
        print('3')
        #s.starttls()
        print('4')
        s.login('app116066240@heroku.com', 'Welcome12#')
        print('5')
        s.sendmail('consult.saurabh@gmail.com', ['consult.saurabh@gmail.com', 'deepagarg617@gmail.com'], msg.as_string())
        print('6')
        s.close()
        print('mail sent')
        return 'Mail sent'
    except Exception as e:
        print('error while sending mail')
        print(e)
        return 'Mail not sent'

mailTest()
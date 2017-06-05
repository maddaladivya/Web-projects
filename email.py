import smtplib

content = 'Here is my first mail using python :)'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('sarvanimini@gmail.com','mini@241098')

mail.sendmail('sarvanimini@gmail.com','k.mounikasmitha999@gmail.com',content)

mail.close()
import smtplib
from email. mime. text import MIMEText
from email. mime. multipart import MIMEMultipart


from_email = 'потча' # почта, котроя специально содана для приложения
password = 'пароль' #пароль от этой почты (лучше держать в отдельной файле config)
msg = MIMEMultipart()
try:
    name = input("Введи имя\n")
    to_email = input("Введи свою почту\n")
except ValueError:
    print("Не правильно введено имя или почта")

message ='Добро пожаловать' +" "+ name + " "+ ',вы разегестрированя на сайте Betonit'

msg. attach (MIMEText (message, 'plain'))

server = smtplib.SMTP('smtp.mail.ru: 587')
server. starttls()
server.login(from_email, password)
server. sendmail (from_email, to_email,msg.as_string())
server.quit()
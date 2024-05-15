import yagmail, ssl

def send_mail(email,object,content):
    yag = yagmail.SMTP(user='themail@gmail.com', password='password')
    yag.send(email, object, content)
import smtplib, ssl


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465

    username = "pronoymalick2004@gmail.com"
    password = "kngk colt stwp rela"

    receiver = "pronoymalick2004@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, user_message)


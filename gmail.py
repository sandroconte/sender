import smtplib
import json

def gmail_server():
    conf = json.load(open('configurations.json', 'r'))
    try:
        server = smtplib.SMTP(conf["smtp_host"], conf["smtp_port"])
        server.ehlo()
        server.starttls()
        server.login(conf["sent_from"], conf["gmail_password"])

        return server
    except Exception as e:
        print(str(e))

    return e
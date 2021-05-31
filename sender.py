import json
from pathlib import Path

conf = json.load(open('configurations.json', 'r'))

from contacts import retrieve_email
from gmail import gmail_server
emails = retrieve_email(Path('assets', 'Customers.xlsx'))

body = "Hey, what's up?\n\n- You"
email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (conf["sent_from"], ", ".join(conf["test_to"]), conf["subject"], body)

server = gmail_server()

try:
    server.sendmail(conf["sent_from"], conf["test_to"], email_text)
    server.close()
except Exception as e:
    print(str(e))
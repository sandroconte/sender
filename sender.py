from pathlib import Path

from contacts import retrieve_email

emails = retrieve_email(Path('assets', 'Customers.xlsx'))

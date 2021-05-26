

def retrieve_email(xlsx_file):
    import re
    import openpyxl

    wb_obj = openpyxl.load_workbook(xlsx_file)

    sheet = wb_obj.active
    regexp = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    emails = sorted({row[1].value.lower() for row in sheet.iter_rows() if row[1].value and regexp.match(row[1].value)})

    return emails

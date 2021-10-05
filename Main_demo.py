from gead import *
from ocr_bsd import *
from folder_demo import get_folder_path
from create_histo import create_histogram
from generate_report import *

messages_filter = 'SUBJECT "Invoices" UNSEEN'

while True:
    var = get_email_attachment_demo('****', "****", filters='SUBJECT "Invoices"')
    var.conn()
    var.get_filtered_emails()
    for email in var.emails_ids:
        body, attachments = var.get_email_content(email)
        for attach in attachments:
            filename, part = attach
            if "Bank" in filename:
                filepath = get_folder_path('Attachments')
                filepath = os.path.join(filepath, filename)
                with open(filepath,'wb')as f:
                    f.write(part.get_payload(decode=True))
                extract_table(filepath)

    # list_attachment = email_attachment_demo('Gmailusername','gmailpw')
    # if list_attachment != []:
    #     for attach in list_attachment:
    #         extract_table(attach)
    #     img_report = create_histogram('Bank_archive.csv')
    #     pdf_file = generate_report(img_report)
    #     print(pdf_file)
    # else:
    #     print('no new email')

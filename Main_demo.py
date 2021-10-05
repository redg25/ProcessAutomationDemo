import os
from gead import *
from ocr_bsd import *
from folder_demo import get_folder_path
from config import user,password
from create_histo import create_histogram
from generate_report import *

messages_filter = 'SUBJECT "Invoices" UNSEEN'

while True:
    var = get_email_attachment_demo(user, password, filters='SUBJECT "Invoices"')
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
                recon_file = extract_table(filepath)
                img_report = create_histogram(recon_file)
                pdf_file = generate_report(img_report)
                print('yeah')


import os
from get_email_invoice import *
from recon_invoices import get_table_from_file, invoices_recon
from manage_att_folders import get_folder_path
from config import user,password
from create_invoice_diagram import create_histogram
from generate_report import *


while True:
    var = get_email_attachment_demo(user, password, filters='SUBJECT "Invoice" UNSEEN')
    var.conn()
    var.get_filtered_emails()
    for email in var.emails_ids:
        body, attachments = var.get_email_content(email)
        for attach in attachments:
            filename, part = attach
            if "invoice" in filename:
                filepath = get_folder_path('Attachments')
                filepath = os.path.join(filepath, filename)
                with open(filepath,'wb')as f:
                    f.write(part.get_payload(decode=True))
                df_file = get_table_from_file(filepath)
                recon_file = invoices_recon(df_file,'recon_invoice_demo.csv')
                img_report = create_histogram(recon_file)
                pdf_file = generate_report(img_report)
                print(f'The report {pdf_file} is ready')


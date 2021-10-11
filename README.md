# ProcessAutomationDemo
author: Regis Corblin <br />
email: regiscorblin@yahoo.fr <br /><br/>
A few python scripts to display what kind of simple process automation can be done with open sources libraries. <br />
The scripts are based on a demo use case where the following steps are automated: <br />
* Extract an attachment (bank statement with inoices payments) from an gmail email received to a auto-managed folder structure (a folder for each day where an email is received)
* Read the table on the pdf in the attachment
* Reconcile the data of new invoices payments with the the database of inovice payment history (csv is this case)
* Generate a bar diagram with the current invoice payments statuses grouped by month.
* Include this diagram in a pre-formatted pdf report.<br/><br/>
The main_demo.py file is used to run the use case. <br/>
The recon_invoice_demo.csv must be in the same folder. <br/>
To pass your gmail user and password, you can harcode them directly in the main_demo.py or create a config.py script to pass them through.<br/>
To trigger the running script, send an email with the Sample_invoice_payment.pdf to your gmail account and make sure the word invoice is in the email subject.

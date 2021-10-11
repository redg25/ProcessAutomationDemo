# ProcessAutomationDemo
author: Regis Corblin <br />
email: regiscorblin@yahoo.fr <br /><br/>
A few python scripts to display what kind of simple process automation can be done with open sources libraries. <br />
The scripts are based on a demo use case where the following steps are automated: <br />
* Extract an attachment (bank statement with inoices payments) from an email received to a auto-managed folder structure (a folder for each day where an email is received)
* Read the table on the pdf in the attachment
* Reconcile the data of new invoices payments with the the database of inovice payment history (csv is this case)
* Generate a bar diagram with the current invoice payments statuses grouped by month.
* Include this diagram in a pre-formatted pdf report.

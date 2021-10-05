import email as em
import imaplib
import base64

class get_email_attachment_demo:

    def __init__(self,user,pw,filters='All',folder='',inbox='Inbox'):
        self.user = user
        self.pw = pw
        self.filters = filters
        self.folder = folder
        self.inbox = inbox

    def conn(self):
        self.mail = imaplib.IMAP4_SSL("imap.gmail.com")
        self.mail.login(self.user, self.pw)

    def get_filtered_emails(self):
        self.mail.select(self.inbox)
        result, ids = self.mail.uid('search', None, self.filters)
        self.emails_ids = ids[0].split()

    def get_email_content(self,id):
        def get_body(email_message):
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    return body
                else:
                    continue
        def get_attachment(email_message):
            list_attachments = []
            for part in email_message.walk():
                if part.get_content_maintype()=='multipart':
                    continue
                if part.get('Content-disposition') is None:
                    continue
                filename = part.get_filename()
                if '=?UTF' in filename:
                    filename = filename[10:]
                    filename = base64.b64decode(filename).decode('utf-8')
                    list_attachments.append((filename,part))
            return list_attachments

        result, email_data = self.mail.uid('fetch', id, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = em.message_from_string(raw_email_string)
        body = get_body(email_message)
        list_attachments = get_attachment(email_message)
        return body, list_attachments


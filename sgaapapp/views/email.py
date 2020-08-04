# import threading
#
# from django.core.mail import EmailMessage
#
# from store.settings import EMAIL_HOST_USER
#
#
# class EmailThread(threading.Thread):
#     def __init__(self, subject, html_content, recipient_list):
#         self.subject = subject
#         self.recipient_list = recipient_list
#         self.html_content = html_content
#         threading.Thread.__init__(self)
#
#     def run (self):
#         msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list)
#         msg.content_subtype = "html"
#         msg.send()
#
# def send_html_mail(subject, html_content, recipient_list):
#     EmailThread(subject, html_content, recipient_list).start()
#

from django.core.mail import send_mail as core_send_mail
from django.core.mail import EmailMultiAlternatives
import threading

from sgaap.settings import EMAIL_HOST_USER


class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        msg.send(self.fail_silently)

def send_mail(subject, body, recipient_list, fail_silently=False, html=None, *args, **kwargs):
    EmailThread(subject, body, EMAIL_HOST_USER, recipient_list, fail_silently, body).start()

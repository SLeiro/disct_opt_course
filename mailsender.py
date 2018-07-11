#!/usr/bin/env python
"""
Send email messages using our Google Apps account
"""

import smtplib

BOT_ADDRESS = 'bot@continentesiete.com'
BOT_USERNAME = 'bot@continentesiete.com'
BOT_PASSWORD = 'Continente7!'
BOT_SERVER_PORT = 'smtp.gmail.com:587'


class MailSender(object):

    def __init__(self):
        self.fromaddr = BOT_ADDRESS
        self.username = BOT_USERNAME
        self.password = BOT_PASSWORD
        self.server = smtplib.SMTP(BOT_SERVER_PORT)

    def send_mail(self, toaddrs, subject, msg):
        text = 'Subject: {}\n\n{}'.format(subject, msg)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.username, self.password)
        self.server.sendmail(self.fromaddr, toaddrs, text)
        self.server.quit()


if __name__ == '__main__':

    for i in range(0, 7, 1):
        ms = MailSender()
        ms.send_mail(
            'cecilia.garcia.l.m@accenture.com',
            'Mail 1',
            'If you can read this, the test was a success. BTW, you suck.'
        )

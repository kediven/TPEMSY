__author__ = "Jonathan Braun"
__version__ = "1.0"
__maintainer__ = "Jonathan Braun"
__email__ = "jonathan.braun@eduvaud.ch"
__status__ = "Production"
__date__ = "February 2023"

#-----------------------------------------------------
# Importing libraries and modules
#-----------------------------------------------------
import datetime                                                             # Library for date and time related stuff
import smtplib                                                              # Library for email related stuff

#-----------------------------------------------------
# Declaring functions
#-----------------------------------------------------
def send_email(receiver, subject, message):
    server = smtplib.SMTP("mail.etml-es.ch")
    server.login("user","password")
    sender = "XXX@etml-es.ch"

    headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Disposition': 'inline',
        'Content-Transfer-Encoding': '8bit',
        'From': sender,
        'To':receiver,
        'Date': datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
        'X-Mailer': 'python',
        'Subject': subject
    }
    # create the message
    msg = ''
    for key, value in headers.items():
        msg += "%s: %s\n" % (key, value)

    # add contents
    msg += "\n%s\n" % (message)

    try:
        server.sendmail(headers['From'], headers['To'], msg.encode("utf8"))
        server.quit()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


#-----------------------------------------------------
# Main script
#-----------------------------------------------------
if __name__ == "__main__":  # Runs only if called as a script but not if imported
    print("Hello This script is a test and will try to send an email")

    # Sending an email to test the function
    subject = "Ceci est un email de test"
    message = "Bonjour! Ceci est un email de test."

    send_email(["matteo.stefanelli@eduvaud.ch"], subject, message)
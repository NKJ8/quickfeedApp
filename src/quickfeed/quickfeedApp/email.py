# mjpemlqvtnmmrbvk

# import smtplib
from django.conf import settings
from django.core.mail import send_mail



subject = 'welcome to GFG world'
message = f'Hi , thank you for registering in geeksforgeeks.'
# message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
email_from = settings.EMAIL_HOST_USER
recipient_list = ["ak@yopmail.com"]
send_mail( subject, message, email_from, recipient_list )



# smtp_server = "smtp.gmail.com"
# port = 587  # For starttls
# sender_email = "akshaysen.sen75@gmail.com"
# receiver_email = "ak@yopmail.com"
# password = "mjpemlqvtnmmrbvk"

# # Create a secure SSL context
# context = ssl.create_default_context()

# # Try to log in to server and send email
# try:
#     server = smtplib.SMTP(smtp_server,port)
#     server.ehlo() # Can be omitted
#     server.starttls(context=context) # Secure the connection
#     server.ehlo() # Can be omitted
#     server.login(sender_email, password)
#     # TODO: Send email here
#     server.sendmail(sender_email, receiver_email, message)
#     print("Email has been sent successfully")
# except Exception as e:
#     # Print any error messages to stdout
#     print(e)
# finally:
#     server.quit() 
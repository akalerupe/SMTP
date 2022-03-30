# import smtplib,ssl

# sender_email = "matukoweye110@gmail.com"
# receiver_email = "matukoweye110@gmail.com"
# message = """\
# Subject: Hi there

# This message is sent from Python."""


# port=465 
# password=input("Please type your gmail password")

# # create a secure ssl context
# context=ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)as server:
#     server.login("matukoweye110@gmail.com",password)

# # initiate the send mail option
# server.sendmail(sender_email,receiver_email,message)
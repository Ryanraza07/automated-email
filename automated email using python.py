#!/usr/bin/env python
# coding: utf-8

# In[2]:


import smtplib

sender_email = "raazaltaf009@gmail.com"
sender_password = "fiay ibke hkux axoq"
recipient_email = "ryanraza001@gmail.com"
subject = "Automated Email"
body = "Hello, this is an automated email sent using Python!"

# Connect to the SMTP server and send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message)

print("Email sent successfully!")


# In[ ]:





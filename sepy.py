# Python code to illustrate Sending mail from your Gmail account with attachment 
# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "shilpamanoj36@gmail.com" 
toaddr = "emil20bcs186@iiitkottayam.ac.in" 
# instance of MIMEMultipart 
msg = MIMEMultipart()
 # storing the senders email address 
msg['From'] = fromaddr 
# storing the receivers email address 
msg['To'] = toaddr 
# storing the subject 
msg['Subject'] ="'Merry Christmas'" 
# string to store the body of the mail 
body = """Good evening 
                          Kindly see the attachment. :) 


                          Thank you 
                           Yours truly 
                          Shilpa Manoj""" 
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
# the file to be sent 
filename = "merry.docx" 
attachment = open("C:/Users/Sia Emil/Desktop/merry.docx",'rb') 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
# To change the payload into encoded form 
p.setpayload((attachment).read()) 
# encode into base64
 encoders.encodebase64(p)
 p.add_header('Content-Disposition', "attachment; filename= %s" % filename)  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
# creates SMTP session 
s = smtplib.smTP('smtp.gmail.com', 587)
# start TLS for security 
s.starttls() 
s.login(fromaddr, "*********")
# Converts the Multipart msg into a string 
text = msg.as_string()
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
# terminating the session 
s.quit() 


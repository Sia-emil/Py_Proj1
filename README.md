# Py_Proj1
Python - Sending Email using SMTP
Python, being a powerful language don’t need any external library to import and 
offers a native library to send emails- “SMTP lib”. “smtplib” creates a Simple 
Mail Transfer Protocol client session object which is used to send emails to any 
valid email id on the internet. Different websites use different port numbers. 
Steps to send mail with Attachments from Gmail account: 
1. First, “smtplib” library needs to be installed. 
2. For adding an attachment, you need to import: 
a) import smtplib 
b) from email.mime.multipart import MIMEMultipart 
c) from email.mime.text import MIMEText 
d) from email.mime.base import MIMEBase 
e) from email import encoders 
These are some libraries which will make our work simple. These are the native 
libraries. 
3. Firstly, create an instance of MIMEMultipart, namely “msg” to begin with. 
4. Mention the sender’s email id, receiver’s email id and the subject in the 
“From”, “To” and “Subject” key of the created instance “msg”. 
5. In a string, write the body of the message you want to send, namely body. 
Now, attach the body with the instance msg using attach function. 
6. Open the file you wish to attach in the “rb” mode. Then create an instance of 
MIMEBase with two parameters. 
 First one is ‘_maintype’ and the other one is ‘_subtype’. This is the base class 
for all the MIME-specific sub-classes of Message. 
Note that ‘_maintype’ is the Content-Type major type (e.g. text or image), 
and ‘_subtype’ is the Content-Type minor type (e.g. plain or gif or other 
media). 
7. set_payload is used to change the payload the encoded form. Encode it in 
encode_base64. And finally attach the file with the MIMEMultipart created 
instance msg. 
8. After that, to create a session, we will be using its instance SMTP to 
encapsulate an SMTP connection. 
s = smtplib.SMTP('smtp.gmail.com', 587) 
In this, you need to pass the first parameter of the server location and 
the second parameter of the port to use. For Gmail, we use port number 
587
9. For security reasons, now put the SMTP connection in the TLS mode. TLS 
(Transport Layer Security) encrypts all the SMTP commands. After that, 
for security and authentication, you need to pass your Gmail account 
credentials in the login instance. The compiler will show an 
authentication error if you enter invalid email id or password. 
10. Store the message you need to send in a variable say, message. 
Using the sendmail() instance, send your message. sendmail() uses 
three parameters: sender_email_id, receiver_email_id and 
message_to_be_sent. 
The parameters need to be in the same sequence. 
This will send the email from your account. After you have completed your task, 
terminate the SMTP session by using quit().

![image](https://user-images.githubusercontent.com/90092525/179489842-9f0db65b-aa20-4597-b4e0-c5bf7b6a5e9e.png)


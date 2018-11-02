import smtplib
import getpass
myemail="your email id: "
password=getpass.getpass()
recemail=input("receiver's email id: ")
#creates smtp session
s=smtplib.SMTP('smtp.gmail.com',587)
#start TLS for security
s.starttls()

s.login(myemail, password)

message="hello"

s.sendmail(myemail, recemail, message)

s.quit()
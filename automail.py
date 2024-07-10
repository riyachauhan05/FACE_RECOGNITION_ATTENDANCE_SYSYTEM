import yagmail
import os
import datetime

date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP(user="prateeksingh0809@gmail.com", password="Defence0809@")

# sent the mail
yag.send(to="singhman2075@gmail.com",
subject=sub, # email subject, 
contents="Attendance of sec D",  # email body
attachments= filename  # file attached  
)
print("Email Sent!")

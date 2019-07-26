import picamera
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage

#Start Camera to capture image and save as test.jpg inside same #folder where script is residing

cam = picamera.PiCamera()
cam.start_preview()
cam.capture('test.jpg')
cam.stop_preview()

#Create message with attachment

msg = MIMEMultipart()
msg.attach(MIMEImage(file("test.jpg").read()))
msg['Subject']='IoT - Heramb MakerLab'

content = 'this is sample'
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('<from_email>@gmail.com','<password>')
mail.sendmail('<from_email>@gmail.com','<to_email>@gmail.com',msg.as_string())
mail.close()

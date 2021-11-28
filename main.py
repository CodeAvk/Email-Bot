import smtplib
import speech_recognition as sr
import pyttsx3
import pyaudio
from email.message import EmailMessage

Assistance=sr.Recognizer()
engine=pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print("listening........")
            voice=Assistance.listen(source)
            info=Assistance.recognize_google(voice) # here we call Google Api to convert text into voice
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver,subject,message):
# Creating a ser:ver to send email to server then send to its destination
    server=smtplib.SMTP("smtp.gmail.com",587) # Here the 1st Argument is SMTP server name in our case its -smtp.gmail.com bcz ill send email by using gmail
                                          # and the second argument is PORT number- in our case port number is 587

    server.starttls() # Ensure server that you are a secret person so that server can trust you
    server.login("avksmlavk@gmail.com","Samal@123")
    email=EmailMessage()
    email['From']="avksmloo@gmail.com"
    email['To']=receiver
    email['Subject']=subject
    server.sendmail("avksmlavk@gmail.com","avksmloo@gmail.com","Hello")
    email.set_content(message)
    server.send_message(email)





email_list={"python":"aswebseriesandmovies@gmail.com",
            "java":"avksmloo@gmail.com"}

def get_email_info():
    talk("Please tell me to whome you want to send email")
    name=get_info()
    receiver=email_list[name]
    print(receiver)
    talk("Sir Please tell me the subject")
    subject=get_info()
    talk("Sir Please tell me the message you want to send")
    message=get_info()
    talk("Sir Your Message is sent")

    send_email(receiver,subject, message)


get_email_info()

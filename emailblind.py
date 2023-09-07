import speech_recognition as sr
import easyimap
import pyttsx3
import smtplib

unm = "mohammedgaffar012@gmail.com"
pwd = "nwohiiufvzijriul"

r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now:"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry Could not recognize what you said"
            speak(str)

def sendmail():

    rec = "nehaneha7812@gmail.com"

    str = "Please speak the body of your email"
    speak(str)
    msg = listen()

    str = "You have spoken the message"
    speak(str)
    speak(msg)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(unm, pwd)
    server.sendmail(unm, rec, msg)
    server.quit()

    str = "The email has been sent"
    speak(str)

def readmail():
    server = e.connect("imap.gmail.com", unm, pwd)
    server.listids()

    str = "Please say the Serial number of the email you wanna read starting from latest"
    speak(str)

    a = listen()
    if( a == "Tu"):
        a= "2"

    b = int(a) - 1

    email = server.mail(server.listids()[b])

    str = "The email is from: "
    speak(str)
    speak(email.from_addr)
    str = "The subject of the email is: "
    speak(str)
    speak(email.title)
    str = "The body of email is: "
    speak(str)
    speak(email.body)

str = "Welcome to voice based emails For Blinds"
speak(str)

while(1):

    str = "What do you want to do?"
    speak(str)

    str = "Speak SEND to Send email   Speak READ to Read Inbox   Speak EXIT to Exit"
    speak(str)

    ch = listen()

    if (ch == 'send'):
        str = "You have Chosen to send an email"
        speak(str)
        sendmail()

    elif ( ch == 'read'):
        str = "You have chosent to read email"
        speak(str)
        readmail()

    elif (ch == 'exit'):
        str = "You have chosen to exit, Bye Bye"
        speak(str)
        exit(1)

    else:
        str = "Invalid choice, you said:"
        speak(str)
        speak(ch)

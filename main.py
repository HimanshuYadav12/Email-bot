import smtplib #simple mail transfer protocol library
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() # transport layer security
    server.login('youremailaddress@gmail.com', 'yourpassword')
    email = EmailMessage()
    email['From'] ='youremailaddress@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

# Make a list of your friends mail addresses

email_list = {
    'friend1': 'friend1@gmail.com',
    'friend2': 'friend2@gmail.com',
    'friend3': 'friend3@gmail.com',
    'friend4 ': 'friend4@gmail.com',
    'friend5': 'friend5@gmail.com',
    }

def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey himanshu. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    else:
        return

get_email_info()
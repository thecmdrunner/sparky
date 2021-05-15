from gtts import gTTS
import speech_recognition as sr
import datetime
from time import ctime
import wikipedia
import webbrowser 
import os
import smtplib
from PyDictionary import PyDictionary
from playsound import playsound


to = ' ' #email address to send email to
doneListening = './audio/done_listening.wav'
dictionary = PyDictionary() #dictionary 


# Fill your own details

yourName = 'Master' # enter your name 
yourMail = '' # enter your mail
botMail = '' # Put your burner email address here, and turn on external access. 
botMailPassword = '' # create a secure password


# Functions

def beep():
    playsound(doneListening)


## TODO: alert and error beeps


def say(words):
    tts = gTTS(text=words, lang='en')
    tts.save("response.mp3")
    playsound('response.mp3')
    os.remove('response.mp3')

def printnsay(words):
    print(words)
    say(words)

def greeting(name):
    printnsay('Hello, I am sparky! What would you like me to do?')
    
def exit_alert():
    exitmsg='Bye for now, tell me when you need something.'
    printnsay(exitmsg)
    exit()

def get_time():
    now = datetime.datetime.now()
    hours = (now.strftime("%H"))
    minutes = (now.strftime("%M"))
    seconds = (now.strftime("%S"))
    string_time = ("it's " +hours+ " hours, " +minutes+ " minutes, and " +seconds+ " seconds")
    return string_time

def mailsetup(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(botMail, botMailPassword)
    server.sendmail(botMail, to, content)
    server.close()


def sendEmail():

    ## TODO: Put subject in email

    if botMailPassword=='':
        printnsay('You need to complete the email setup first.')
        exit()

    beep()
    try:
        printnsay('whom would you like to send?')
        beep()

        recipientName = str.lower(takeCommand())
               
        if recipientName == yourName:
            to = yourMail

        elif recipientName == "PERSON 1":
            to = "THEIR EMAIL"

        elif recipientName == "PERSON 2":
            to = "THEIR EMAIL"

        elif recipientName == "PERSON 3":
            to = "THEIR EMAIL"         
              
        beep()
        printnsay('What would you like to send?')
        beep()
        message = takeCommand()
        content = str(message + " P.S. This mail was sent by Sparky, requested by user "+yourName+".")  

        mailsetup(to, content)
        beep()
        emailSentResponse = "Your mail has been sent!"
        printnsay(emailSentResponse)
        beep()
               

    except Exception as e:
        beep()
        print(e)
        say("Sorry "+yourName+", email is currently facing some issues. Please wait for a while and try again later.")    


def takeCommand():

    # take microphone input from the user and returns a string output

    print('Now say something')

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.pause_threshold = 1.5
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")    
        audiowords = recognizer.recognize_google(audio, language='en-in')
        print("You said: ",audiowords,"\n")

    except Exception :
        # print(e)    
        print("Say that again please...")  
        return "None"

    return audiowords


def respond(query):

    try:

        print("You said: " + query)

        if query == 'None':
            return 0
        
        elif 'time' in query:
            current_time = get_time()
            beep()
            printnsay(current_time)

        elif 'what is my name' in query:
            beep()
            printnsay('Your name is '+yourName+', and I hope you dont forget it again... haahaa')

        elif 'send an email' in query:
            sendEmail()

        elif ('bye' or 'exit' or 'shut down' or 'shutdown') in query: 
            beep()
            printnsay("Turning off!")
            exit_alert()

    except Exception as e:
        beep()
        say("sorry, i didn't get what you said.")
        print('\nPlease say again...\n')

if __name__ == "__main__":
   
    #hello()
    #exit()

    beep()

    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<12:
        dayphase='morning'
    
    elif hour>=12 and hour<16:
        dayphase='afternoon'

    else:
        dayphase='evening'

    printnsay('Good '+dayphase+', thanks for using sparky!')
    greeting(yourName)

    while True:
        beep()
        order = takeCommand()
        respond(order)

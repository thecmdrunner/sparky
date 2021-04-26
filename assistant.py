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

# Fill your own details

yourName = 'Pranav' # put your name here
botMail = '' # Put your burner email address here, after turning on external access. 
botMailPassword = '' 

# Dont touch
to = ' ' #email address to send email to
doneListening = './audio/done_listening.wav'
dictionary = PyDictionary() #dictionary 


def say(words):
    tts = gTTS(text=words, lang='en')
    tts.save("response.mp3")
    playsound('response.mp3')
    os.remove('response.mp3')

def printandsay(words):
    print(words)
    say(words)

def greeting(USER):
    printandsay('')
    
def exit_alert():
    say("Due to the pandemic of Corona Virus, I insist you to not use me. Exiting....")
    print("Due to the pandemic of Corona Virus, I insist you to not use me. Exiting....")
    exit()

def get_time():
    now = datetime.datetime.now()
    hours = (now.strftime("%H"))
    minutes = (now.strftime("%M"))
    seconds = (now.strftime("%S"))
    string_time = ("it's " + hours + " hours, " + minutes + " minutes, and " + seconds + " seconds")

def takeCommand():

    #It takes microphone input from the user and returns a string output hehe

    print('Now say something')

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.pause_threshold = 1.5
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")    
        query = recognizer.recognize_google(audio, language='en-in')
        print("You said: ",query,"\n")

    except Exception :
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(botMail, botMailPassword)
    server.sendmail(botMail, to, content)
    server.close()

def respond(query):

    try:

        print("You said: " + query)

        if query == 'None':
            return 0
        
        elif 'time' in query:
            get_time()
            playsound(doneListening)
            printnsay(string_time)

        elif 'what is my name' in query:
            playsound(doneListening)
            printnsay1('Your name is '+yourName+', and I hope you dont forget it again... haahaa')

        elif 'send an email' in query:

            ## Put subject in email

            playsound(doneListening)
            try:
                printnsay('whom would you like to send?')
                playsound(doneListening)
                
                recipientName = str.lower(takeCommand())
                
                if recipientName == "ME":
                    to = "MY EMAIL"

                elif recipientName == "PERSON 2":
                    to = "THEIR EMAIL"         
      
                
                printnsay('What would you like to send?')
                playsound(doneListening)
                message = takeCommand()
                content = str(message + " P.S. This mail was sent by Edith, requested by user "+yourName+".")  

                sendEmail(to, content)
                emailSentResponse = "Your mail has been sent!"
                playsound(doneListening)
                printnsay(emailSentResponse)
                

            except Exception as e:
                playsound('done_listening.wav')
                print(e)
                say("Sorry "+yourName+", email is currently facing some issues. Please wait for a while and try again later.")    


        elif ('bye' or 'shut down' or 'shutdown') in query: 
            playsound(doneListening)
            printnsay("Turning off!")
            exit_alert()

    except Exception as e:
        playsound(doneListening)
        say("i am sorry, i didn't get what you said.")
        print('\nPlease say again...\n')

if __name__ == "__main__":
   
    #hello()
    #exit()
    playsound(doneListening)
    greeting(yourName)
    while True:
    # if 1:
     playsound(doneListening)

     query = takeCommand()
     respond(query)

     

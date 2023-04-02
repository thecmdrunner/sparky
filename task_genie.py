# Trying out chatGPT api with voice commands.

import speech_recognition as sr
import datetime
from time import ctime
import os
from playsound import playsound

doneListening = './audio/done_listening.wav'


# Fill your own details

yourName = 'Master'  # enter your name


def beep():
    playsound(doneListening)


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
        print("You said: ", audiowords, "\n")

    except Exception as e:
        print(e)
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
            printnsay('Your name is '+yourName +
                      ', and I hope you dont forget it again... haahaa')

        elif 'send an email' in query:
            sendEmail()

        elif ('bye' or 'exit' or 'shut down' or 'shutdown') in query:
            beep()
            printnsay("Turning off!")
            exit_alert()

    except Exception as e:
        beep()
        print("sorry, i didn't get what you said.")
        print('\nPlease say again...\n')


if __name__ == "__main__":
    beep()
    while True:
        beep()
        order = takeCommand()
        respond(order)

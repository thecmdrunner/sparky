# Trying out chatGPT api with voice commands.

import speech_recognition as sr
import datetime
from time import ctime
import os
from playsound import playsound
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

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

        elif ('bye' or 'exit' or 'shut down' or 'shutdown') in query:
            beep()
            print("Turning off!")
            exit()

        # generate a response using OpenAI ChatGPT API
        prompt = f"What is your opinion on {query}?"
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                  messages=[{
                                                      "role": "user",
                                                      "content": prompt
                                                  }])

        print(completion)

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

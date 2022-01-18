import pyttsx3 
import speech_recognition as sr
import datetime
from time import ctime
import wikipedia 
import webbrowser # opens in internet explorer by default sorry :p
import os
import smtplib
from PyDictionary import PyDictionary


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
 # print(voices[1].id)
engine.setProperty('voice', voices[0].id)


dictionary = PyDictionary() #dictionary 


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # specifically for my machine

to = ' ' #email address to send email to

def say(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Sir! Jarvis at your service . How may I help you this time?")
        say("Good Morning Sir! Jarvis at your service . How may I help you this time?")

    elif hour>=12 and hour<18:
        print("Good Afternoon Sir! Jarvis at your service . How may I help you this time?")
        say("Good Afternoon Sir! Jarvis at your service . How may I help you this time?")   

    else:
        print("Good Evening Sir! Jarvis at your service . How may I help you this time?")  
        say("Good Evening Sir! Jarvis at your service . How may I help you this time?")  

    

def takeCommand():
    #It takes microphone input from the user and returns a string output hehe

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
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
    server.login('mail', 'pass')
    server.sendmail('mail', to, content)
    server.close()




if __name__ == "__main__":
    print('*********************************************************Welcome***To***Jarvis********************************************************************')
    
    wishMe()
    print('*********************************************************Welcome***To***Jarvis********************************************************************')
    
    while True:
    # if 1:
        query = takeCommand().lower()
       
        if 'wikipedia' in query:
           try:
                say('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                say("According to Wikipedia")
                print(results)
                say(results)
                say('Anything else you would like me to do sir?')
           except Exception as e:
                print(e)
                say('sorry sir, there is no discrete article available for that word. You might wanna say something in a particular context.') 

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open_new_tab("youtube.com")

        elif 'open google' in query:
           webbrowser.get(chrome_path).open_new_tab("google.com")

        elif 'open bing' in query:
           webbrowser.get(chrome_path).open_new_tab("bing.com")   

        elif 'open stack overflow' in query:
           webbrowser.get(chrome_path).open_new_tab("stackoverflow.com")   
        elif 'open stackoverflow' in query:
           webbrowser.get(chrome_path).open_new_tab("stackoverflow.com")   
        elif 'open stack over flow' in query:
           webbrowser.get(chrome_path).open_new_tab("stackoverflow.com")   
        elif 'open stackover flow' in query:
           webbrowser.get(chrome_path).open_new_tab("stackoverflow.com")            


        elif 'Hey Jarvis play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play songs' in query:
            music_dir = 'C:\\Songs (PC)\\music and stuff\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))    

        elif 'what is time' in query:
           hours = int(datetime.datetime.now().hour)
           minutes = int(datetime.datetime.now().minute) 
           wordminute = str(minutes)
           seconds = int(datetime.datetime.now().second)
           timeStrFinal = ("it is ",hours," hours ",wordminute," minutes and ",seconds," seconds ")
           print(timeStrFinal)
           say(timeStrFinal)
            

        elif 'open code' in query:
            codePath = "C:\\Users\\prana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

       

        elif 'send an email' in query:
            try:
                
                say("whom should i send?")
                recipientName = str.lower(takeCommand())
                
                if recipientName == "pranav":
                    to = "me@gmail.com"
               
                
                print('What would you like to send?')
                say('What would you like to send?')
                content = takeCommand()  
                sendEmail(to, content)
                emailSentResponse = "Your Email has been sent sir! Anything else you would like me to do sir?"
                print(emailSentResponse)
                say(emailSentResponse)
                

            except Exception as e:
                print(e)
                say("Sorry Sir, email is currently facing some issues. Please wait for a while and try again later. Anything else you would like me to do?")    

        
        elif 'open dictionary' in query: 
             try:
                say("Opening dictionary... which word are you looking for?")
                content = takeCommand()
                say(dictionary.googlemeaning(content, formatted=True))
             except Exception as e:    
                print(e)
                say("Sorry Sir, an unexpected error occured. Please look into the console and try to analyze it. Anything else you would like me to do ?")  
            
        elif 'can you change your voice' in query: 
            say('i get that i sound like a very early prototype of AI. but eventually, my voice get more pleasing and delightful sir.')

        elif 'who are you' in query: 
            say('oh hey i am Tony Stark''s Jarvis, and i am always here in these glasses.')    
        
        elif 'what my name' in query:
            say('your name is pranav kulkarni. and i hope you dont forget it again haha')

        elif 'who do you think is god' in query:
            say('according to my database, god is someone who either has made us and we consist of god; or god is the most powerful person or object and humans worship him')
        
        elif 'whats my schedule' in query:
            _day = datetime.datetime.now()
            currentDay = _day.strftime("%A")
            print("Pranav, it's ",currentDay," today. So not much")

        
        elif "where is" in query:
            query= query.split(" ")
            location = query[2]
            say("Hold on, I will show you where " + location + " is.")
            webbrowser.get(chrome_path).open_new_tab("https://www.google.com/maps/place/" + location + "/&amp;")

        elif "tell me time" in query:
            say(ctime())

        elif 'bye' in query:        
            exit()

        elif 'shut down' in query:        
            exit()

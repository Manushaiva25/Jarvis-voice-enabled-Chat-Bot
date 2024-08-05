import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import datetime

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[1].id)
Assistant.setProperty('rate',170)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    Assistant.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Namaskara sir, good morning")
    elif hour>=12 and hour<18:
        Speak("Namaskara sir, good afternoon")
    else:
        Speak("Namaskara sir, good evening")
    Speak("i am jarvis,please tell me how may i help you")           

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.......")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")
        except Exception as Error:
            Speak("I'm sorry, I didn't catch that. can you please repeat? ")
            return "none"
        return query
        
    
def TaskExe():
    def Music():
        Speak("Tell me the anem of the song!")
        musicName = takecommand()
        pywhatkit.playonyt(musicName)

    def Whatsapp():
        Speak("tell Me the name of the person!")
        name = takecommand()

        if 'Sanjay' in name:
            Speak("tell Me the Message!")
            msg = takecommand()
            Speak("Got the message SIR, What Time i should send this message")
            Speak("Time the hour!")
            hour  = int(takecommand())
            Speak("Time in munute!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+917026993400",msg,hour,min,15)
            Speak("Done Sir, your Message is successfully sent !")
        
        else:
            Speak("tell Me the phone number!")
            phone = takecommand()
            ph = "+91{}".format(phone)
            Speak("tell Me the Message!")
            msg = takecommand()
            Speak("Got the message SIR, What Time i should send this message")
            Speak("Time the hour!")
            hour  = (takecommand())
            Speak("Time in minute!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("OK Sir, your Message will be sent at the specified time !")


    while True:
        query = takecommand()

        if 'hello' in query:
            wishMe()
           
        elif 'how are you Jarvis' in query:
            Speak("I am fine Sir")
            Speak("Whats About You?")

        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strTime}")

        elif 'YouTube search' in query:
            Speak("Ok Sir, This is what i found on your Youtube Search!")
            query = query.replace("jarvis","")
            query = query.replace("Youtube search","")
            web = "https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
            Speak("Done Sir")

        elif 'Google search' in query:
            Speak("Ok Sir, This is what i found on your Google Search!")
            query = query.replace("Jarvis","")
            query = query.replace("Google search","")
            pywhatkit.search(query)
            Speak("Done Sir")
        
        elif 'website' in query:
            Speak("Ok Sir, launching website ")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = 'https://www.{}.com'.format(web1)
            webbrowser.open(web2)
            Speak("Done Sir")

        elif 'launch' in query:
            Speak("tell me the name of the website!")
            name  = takecommand()
            web = 'https://www.{}.com'.format(name)
            webbrowser.open(web)
            Speak("Done Sir!")
        
        elif 'music' in query:
            Music()

        elif 'Wikipedia' in query:
            Speak("Searching on wikipedia..... ")
            query = query.replace("Jarvis","")
            query = query.replace("Wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According to wikipedia : {wiki}")

        elif 'WhatsApp' in query:
            Whatsapp()

        elif 'ok bye' in query:
            Speak("Ok Sir Bye! you can call me anytime, have a graet day")
            break

TaskExe()

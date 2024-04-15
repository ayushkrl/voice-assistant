import pyttsx3
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr 
import webbrowser
import pywhatkit
import os
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices',voices[3].id)
engine.setProperty('rate',170)

def Speak(audio):
    
    print("     ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    #Speak("Hello Sir, How are you?")

def gtts_Speak(audio):
    kk = gTTS(audio)
    kk.save('Assist.mp3')
    playsound('Assist.mp3')
    #gtts_Speak("Hello Sir, Aap kawn ho")

def file_Speak(path):
    #ttsmp3.com
    playsound(path)
    #file_Speak("D:\\Voice Assistant AI\\Database\\Sounds\\Welcome.mp3")

def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source)
        print(": Listening.....")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command: {query}\n")

    except:
        return "NONE"
    
    #DATABASE
    """
    kk = open('Data.txt', 'rb')
    kk.write(f": {query}")
    kk.close()
    """

    return query.lower()
    """
    Speak("Please speak your commands")
    query = TakeCommand()

    if 'hello' in query:
        Speak("Hello sir")

    else:
        Speak("No command found")
    """

def TakeCommand_Hindi():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening.....")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='hi')

        print(f": Your Command: {query}\n")

    except:
        return ""
    
    #DATABASE
    #kk = open('Data.txt', 'rb')
    #kk.write(f": {query}")
    #kk.close()

    return query.lower()
    
def TaskExecution():

    def Music():
        Speak("Tell me the name of the song!")
        musicName = TakeCommand()

        if 'favourite' in musicName:
            os.startfile('D:\Voice Assistant AI\Database\Sounds\Dont you worry child.mp3')
        
        else:
            pywhatkit.playonyt(musicName)

        Speak("Your song has been started , Enjoy sir!")

    def Whatsapp():
        Speak("Tell me the name of the person!")
        name = TakeCommand()

        if 'akshita' in name:
            Speak("Tell me the message sir!")
            msg = TakeCommand()
            Speak("Tell me the time sir!")
            Speak("Tell Hour!")
            hour = int(TakeCommand())
            Speak("Tell Minutes!")
            min = int(TakeCommand())
            pywhatkit.sendwhatmsg("+916206468077",msg,hour,min,3)
            Speak("Okay sir, Sending Whatsapp message!")
        
        else:
            Speak("Tell me the phone number!")
            phone = int(TakeCommand())
            ph = '+91' + phone
            Speak("Tell me the message sir!")
            msg = TakeCommand()
            Speak("Tell me the time sir!")
            Speak("Tell Hour!")
            hour = int(TakeCommand())
            Speak("Tell Minutes!")
            min = int(TakeCommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("Okay sir, Sending Whatsapp message!")
        
    while True:

        query = TakeCommand()

        if 'hello' in query:
            Speak("Hello sir, I am your personal voice assistamt")
            Speak("How may I help you")

        elif 'speech to text' in query:
            Speak("Okay Sir")
            print(f": {audio}")

        elif 'how are you' in query:
            Speak("I am fine sir")
            Speak("How about you?")
        
        elif 'you need a break' in query:
            Speak("Ok Sir, You can call me anytime")
            break
        
        elif 'bye' in query:
            Speak("Okay Sir, Bye!")
            break

        elif 'youtube search' in query:
            Speak("Okay Sir, This is what I found for your search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")
        
        elif 'google search' in query:
            Speak("Okay Sir, This is what I found for your search!")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir!")
            """url = f"https://google.com/search?q={query}"
            webbrowser.open_new_tab(url)"""

        elif 'website' in query:

            Speak("Okay Sir, Launching")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            
            website = 'https://www.' + web1.replace(" ","") + '.com'
            webbrowser.open(website)
            Speak("Launched!")
        
        elif 'launch' in query:

            Speak("Tell me the name of website!")
            name = TakeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")
        
        elif 'facebook' in query:
            Speak("Okay Sir")
            webbrowser.open("https://www.facebook.com")
            Speak("Done Sir!")
        
        elif 'twitter' in query:
            Speak("Okay Sir")
            webbrowser.open("https://www.twitter.com")
            Speak("Done Sir!")

        elif 'instagram' in query:
            Speak("Okay Sir")
            webbrowser.open("https://www.instagram.com")
            Speak("Done Sir!")

        elif 'amazon' in query:
            Speak("Okay Sir")
            webbrowser.open("https://www.amazon.com")
            Speak("Done Sir!")

        elif 'flipkart' in query:
            Speak("Okay Sir")
            webbrowser.open("https://www.flipkart.com")
            Speak("Done Sir!")
        
        elif 'cricbuzz' in query:
            Speak("Okay Sir")
            webbrowser.open("https://www.cricbuzz.com")
            Speak("Done Sir!")

        elif 'music' in query:
            Music()
        
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("assistant","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,5)
            Speak(f"According to Wikipedia : {wiki}")

        elif 'whatsapp' in query:
            Whatsapp()
        
        else:
            Speak("Not recognized")

TakeCommand()
input("Please enter your command")

"""
How to change voices
How to change speech rate (default - 200)
Assistant stuck at listening mode
Youtube search
Google Search
Open a Website
launch Facebook
Wikipedia search
Music play
"""
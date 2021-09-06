import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import wikipedia


#listen to out microphone and return the audio as text using google

def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print('I am listening')
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            speaking("Sorry I did not understand")
            return "I am waiting"
        except sr.RequestError:
            speaking('Sorry the service is down')
            return "I am waiting"
        except:
            return "I am waiting"

transform()

def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
	
speaking('hello world')

engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)
	
id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice',id)
engine.say('Hello World')
engine.runAndWait()

#return the weekend name
def query_day():
    day = datetime.date.today()
    #print(day)
    weekday = day.weekday()
    #print(weekday)
    mapping = {
        0: 'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        speaking(f'Today is {mapping[weekday]}')
    except:
        pass
		
query_day()

#returns the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"{time[1]} o'clock and {time[3:5]} minutes")
	
query_time()

#Intro Greeting at startup
def whatsup():
    speaking('''Hi, I am Tokyo. 
    How may I help you?
    ''')
	
whatsup()

#the heart of our assistant, take queries and return answer
def querying():
    whatsup()
    start = True
    while(start):
        q = transform().lower()
        
        if 'start youtube' in q:
            speaking('starting youtube. Just a second.')
            webbrowser.open('https://www.youtube.com')
            continue
            
        elif 'start webbrowser' in q:
            speaking('starting browser')
            webbrowser.open('https://www.google.com')
            continue
            
        elif 'what day is it' in q:
            query_day()
            continue
            
        elif 'what time is it' in q:
            query_time()
            continue

        elif "bye" in q:
            speaking('ok bye, have a great day')
            break
        
        elif "from wikipedia" in q:
            speaking('checking wikipedia')
            q = q.replace("wikipedia","")
            result = wikipedia.summary(q,sentences=2)
            speaking('found on wikipedia')
            speaking(result)
            continue
            
        elif "your name" in q:
            speaking('I am Tokyo. Your Virtual Assistance')
            continue
            
        elif "search web" in q:
            pywhatkit.search(q)
            speaking('that is what I found')
            continue
            
        elif "play" in q:
            speaking(f'playing {q}')
            pywhatkit.playonyt(q)
            continue
            
        elif "joke" in q:
            speaking(pyjokes.get_jokes())
            continue
            
        elif "stock price" in q:
            search = q.split("of")[-1].strip()
            lookup = {'apple':'AAPL',
                     'amazon':'AMZN',
                      'google':'GOOGLE'
                     }
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketPrice"]
                speaking(f'found it, the price for {search} is {currentprice}')
                continue
            except:
                speaking(f'sorry I have no data for {search}')
            continue
    

querying()

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Qurrata!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Qurrata!")

    else:
        speak("Good Evening Qurrata")

    speak("I'm jerry, tell me how may i help you.?")
    
def takeCommand():
    #It takes microphone input and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.record(source,duration=3)


    try:
        print("Recognixing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")


    except Exception as e:
       # print(e)
        print("Say That Again Please..")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('qurratainin@gmail.com', '******')
    server.sendmail('qurratainin@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    #speak("Qurrata Is A Good Girl")
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Ok Qurrata madam please wait few time")
            print('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'tell me' in query:
            speak("Ok Qurrata madam please wait few time")
            print('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'Whats your name' in query:
            speak("My name is jerry, thanks")
            print("Jerry, Thank You.")


        elif 'how are you' in query:
            speak('Im fine, thank you madam and whats about you.?')
            print("Im fine, thank you madam")
            content = takeCommand()
        
        elif 'who are you' in query:
            speak('My name is jerry,i am your virtual assistent')
            print("Im jerry, your virtual assistent thank you madam")
            content = takeCommand()

       
        elif 'who am i' in query:
            speak('According Your information, your name is Qurrata Inninin and your institute name Metropolitan university.Your deparment name is computer science and engineering,your id number is 161 115 132')
            print("Qurrata Ainin, student of Metropolitan University.")
            content = takeCommand()

        elif 'open youtube' in query:
            speak("Ok Qurrata madam, open youtube right now.")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Ok Qurrata madam, open google right now.")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Ok Qurrata madam, open stackoverflow right now.")
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            speak("Ok Qurrata madam, open facebook right now.")
            webbrowser.open("facebook.com")

        elif 'open github' in query:
            speak("Ok Qurrata madam, open github right now.")
            webbrowser.open("https://github.com")

        elif 'play music' in query:
            speak("Ok Qurrata madam, playing music right now.")
            music_dir = 'F:\\MP3'
            songs = os.listdir(music_dir)
            #sprint(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play videos' in query:
            speak("Ok Qurrata madam, playing video right now.")
            music_dir = 'F:\\Videos'
            songs = os.listdir(music_dir)
            #sprint(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"madam, The time is {strTime}")


        elif 'send email to your madam' in query:
            try:
                speak("what should i say..?")
                content = takeCommand()
                to = "qurratainin@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent.!")

            except Exception as e:
                print(e)
                speak("Sorry Qurrata madam, I'm bot able to send this Email.")

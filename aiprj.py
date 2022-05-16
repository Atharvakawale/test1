import speech_recognition as sr
from GoogleNews import GoogleNews
import pyttsx3
import webbrowser

googlenews = GoogleNews()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything..')
        recordedaudio = recognizer.listen(source, timeout=1)
        print("Done recording..!")
    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print('Your message:', format(text))


    except Exception as ex:
        print(ex)

    if 'youtube' in text:
        b = 'opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    if 'cricket' in text:
        engine.say('cricket news')
        engine.runAndWait()
        googlenews.get_news('cricket')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

cmd()
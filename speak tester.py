import pyttsx3

speak_engine = pyttsx3.init('sapi5')
voices = speak_engine.getProperty(name = 'voices')
speak_engine.setProperty(name = 'voice',value = voices[0].id)
speak_engine.setProperty(name = 'rate' , value = 130)

def speak(speech):
    speak_engine.say(speech)
    speak_engine.runAndWait()

sample='hello boss, lets get our coding freak on'

try:
    speak(sample)
except:
    print('error!',Exception)

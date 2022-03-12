import pyttsx3,pyperclip
speak_engine = pyttsx3.init()
voices = speak_engine.getProperty(name = 'voices')
speak_engine.setProperty(name = 'voice',value = voices[0].id)
speak_engine.setProperty(name = 'rate' , value = 160)
def speak(speech):
    speak_engine.say(speech)
    speak_engine.runAndWait()
def ReadOutLoud() -> None:
    try:
        if (1):
            print('Reading...')
            pyperclip.waitForNewPaste()
            print('speaking...')
            speak(pyperclip.paste())
    except:
        print('Error!')

ReadOutLoud()
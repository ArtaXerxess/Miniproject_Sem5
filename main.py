__title__ = 'Voice Assistant'
__author__ = 'Harshvardhan Singh'

import pyttsx3
import speech_recognition
import os
import pickle
import wikipedia
import webbrowser

class FileSearchEngine:
    def __init__(self):
        self.file_index = [] 
        self.results = [] 
        self.matches = 0 
        self.records = 0
    def create_new_index(self, root_path):
        self.file_index = [(root,files) for root,dirs,files in os.walk(root_path) if files]
        with open('file_index.pkl','wb') as foo:
            pickle.dump(self.file_index,foo)
            foo.close()
    def load_existing_index(self):
        try:
            with open('file_index.pkl','rb') as foo:
                self.file_index = pickle.load(foo)
                foo.close()
        except:
            self.file_index = []
    def search(self,term,search_type='contains'):
        self.matches = 0
        self.records = 0
        self.results.clear()
        for path, files in self.file_index:
            for file in files:
                self.records += 1
                if (search_type == 'contains' and term.lower() in file.lower() or
                search_type == 'startswith' and file.lower().startswith(term.lower()) or 
                search_type == 'endswith' and file.lower().endswith(term.lower())):
                    result = path.replace('\\','/') + '/' + file
                    self.results.append(result)
                    self.matches += 1
                else:
                    continue
        with open('search_results.txt','w') as f:
            f.write('name of file:{}\n'.format(term))
            f.write('{} Matches Found!\n'.format(self.matches))
            for row in self.results:
                f.write(row+'\n')
            f.close()

def find_the_file(file_name):
    path = 'C:/Users/WiiN10pro'
    print('Finding {}...'.format(file_name))
    Guddu= FileSearchEngine()
    Guddu.create_new_index(path)
    Guddu.search(file_name)
    speak('Files containing the name {} are found.\nI have {}matches'.format(file_name,Guddu.matches))

speak_engine = pyttsx3.init('sapi5')
voices = speak_engine.getProperty(name = 'voices')
speak_engine.setProperty(name = 'voice',value = voices[0].id)
speak_engine.setProperty(name = 'rate' , value = 180)
def speak(speech):
    speak_engine.say(speech)
    speak_engine.runAndWait()
def takeCommand():
    '''
    takes input from the microphone, converts it into string
    '''
    recg = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic_source:
        print('Please Speak...')
        print('Listening...')
        recg.pause_threshold = 1
        audio = recg.listen(source=mic_source)
        try:
            print('Recognizing...')
            query = str(recg.recognize_google(audio_data=audio,language='en-in')).lower()
            print('user said: {}'.format(query))
        except:
            print('Error!\nSay that again please')
            return 'None'
        return query



def listen():
    speak('hello, how may i help you?')
    query = takeCommand()
    ChromePath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    if 'find' in query:
        query = query.replace('find ','')
        find_the_file(query)
    elif 'wikipedia ' in query:
        query = query.replace('wikipedia ', '')
        results = wikipedia.summary(query,sentences = 2)
        print(results,'\n')
        speak(results)
    elif 'open youtube' in query:
        print('Opening YouTube...')
        speak('Opening YouTube')
        webbrowser.open('youtube.com')
    elif 'open chrome' in query:
        os.startfile(ChromePath)
    elif 'play' in query:
        songpath = 'C:/Users/Admin/Desktop'
        foo = FileSearchEngine()
        foo.create_new_index(songpath)
        query = query.replace('play ','')
        foo.search(query)
        if foo.results is not None:
            f=str(foo.results[0]).split('/')[-2]
            speak('Song {}, is found in the directory named: {}'.format(query,f))
            os.startfile(foo.results[0])
        

# Main
if __name__ == '__main__':
    listen()
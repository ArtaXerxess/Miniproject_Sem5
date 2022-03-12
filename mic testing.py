import speech_recognition
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

print(takeCommand())
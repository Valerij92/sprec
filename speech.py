import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Скажите что-нибудь')
    audio = r.listen(source)

    try:
        text =r.recognize_google(audio)
        print('Вы сказали :{}'.format(text))
    except:
        print ('Невозможно распознать вашу речь')
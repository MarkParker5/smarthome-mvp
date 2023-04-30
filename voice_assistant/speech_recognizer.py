import speech_recognition as sr
import config


r = sr.Recognizer()
m = sr.Microphone(1)

def reset():
    global r, m
    r = sr.Recognizer()
    m = sr.Microphone(1)
    r.pause_threshold          = 1
    r.energy_threshold         = 2000
    r.dynamic_energy_threshold = True
    r.non_speaking_duration    = 0.5

def listen_noise():
    with m as source:
        r.adjust_for_ambient_noise(source)

def listen():
    reset()
    try:
        with m as source:
            audio = r.listen(source)
    except:
        return ''
    try:
        responce = {'text': r.recognize_google(audio, language = config.language_code).lower(), 'status': 'ok'}
    except sr.UnknownValueError:
        responce = {'text': None, 'status': 'void'}
    except sr.RequestError:
        responce = {'text': None, 'status': 'error'}
    return responce

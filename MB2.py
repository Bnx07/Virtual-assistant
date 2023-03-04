import speech_recognition as sr
import pyttsx3, pywhatkit

name = ["madbone", 'bone', 'mad', 'boom']
listener = sr.Recognizer()
listener.energy_threshold = 3000
listener.dynamic_energy_threshold = False
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("escuchando...")
            listener.adjust_for_ambient_noise(source)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()  
    except:
        pass
    return rec

def runMadbone():
    talk("Despertado y listo para ayudar.")
    while True:
        rec = listen()
        print(rec)
        for n in name:
            if n in rec:
                if "hola" in rec:
                    talk("Hola caballero")
                break
        

runMadbone()
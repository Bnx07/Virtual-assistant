import pyttsx3, pywhatkit
import speech_recognition as sr

class Assistant:
    def __init__(self, name:list, sensibilidad:int):
        self.name = name
        self.listener = sr.Recognizer()
        self.listener.energy_threshold = sensibilidad
        self.listener.dynamic_energy_threshold = False
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def comandos(self, rec:list):
        commands_keys = ["reproduce", "patata"]
        cmd = ""
        for a in commands_keys:
                if a in rec:
                    pos = rec.index(a)+1
                    cmd = a
                    rec = rec[pos:]
                    break
        match cmd:
             case 'reproduce':
                  self.reproduce(" ".join(rec))

    def reproduce(self, rec):
        print(f"Reproduciendo {rec}")
        self.talk(f"Reproduciendo {rec}")
        pywhatkit.playonyt(rec)

    def talk(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        try:
            with sr.Microphone() as source:
                print("escuchando...")
                self.listener.adjust_for_ambient_noise(source)
                pc = self.listener.listen(source)
                rec = self.listener.recognize_google(pc, language="es")
                rec = rec.lower()  
        except:
            pass
        return rec

    def runMadbone(self):
        self.talk("Despertado y listo para ayudar.")
        while True:
            rec = self.listen()
            #rec = input()
            print("entendi:     " + rec)
            for n in self.name:
                if n in rec:
                    rec = rec.replace(n, "")
                    rec = rec.strip().split()
                    self.comandos(rec)
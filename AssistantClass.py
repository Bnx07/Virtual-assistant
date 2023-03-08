import pyttsx3, pywhatkit, os
import speech_recognition as sr
from subprocess import check_output

class Assistant:
    def __init__(self, name:list, sensibilidad:int):
        self.name = name
        self.listener = sr.Recognizer()
        self.listener.energy_threshold = sensibilidad
        self.listener.dynamic_energy_threshold = False
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.remplazo = {'á':'a', 'é':'e', 'í':'i',  'ó':'o', 'ú':'u'}

    def comandos(self, rec:list):
        commands_keys = ["reproduce", "patata", 'whatsapp', 'screenshot', 'captura', 'pantalla']
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
            case 'whatsapp':
                self.whatsapp()
            case 'captura':
                self.captura()
            case 'screenshot':
                self.captura()

    def reproduce(self, rec):
        print(f"Reproduciendo {rec}")
        self.talk(f"Reproduciendo {rec}")
        pywhatkit.playonyt(rec)
    
    def whatsapp(self, msg='', quien=''):
        if msg == '' and quien == '':
            if pywhatkit.open_web(): self.talk("Whatsapp web abierto")

    def captura(self):
        pywhatkit.take_screenshot("MB_screenshot", show=False)
        self.talk('Captura de pantalla tomada con exito... quiere ver la captura?')
        rec = self.listen()
        if 'si' in rec: check_output(os.getcwd()+f'/MB_screenshot.png', shell=True)

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
                for a in rec: 
                    if a in self.remplazo: rec = rec.replace(a, self.remplazo[a])
        except:
            pass
        return rec

    def runMadbone(self, manual=False):
        self.talk("Despertado y listo para ayudar.")
        while True:
            if not manual: rec = self.listen()
            else: 
                rec = input()
                for a in rec: 
                    if a in self.remplazo: rec = rec.replace(a, self.remplazo[a])
            print("entendi:     " + rec)
            for n in self.name:
                if n in rec:
                    rec = rec.replace(n, "")
                    rec = rec.strip().split()
                    self.comandos(rec)
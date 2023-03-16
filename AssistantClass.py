import pyttsx3, pywhatkit, os
import speech_recognition as sr
from subprocess import check_output
from Commands import commands, commandReproduce, commandWhatsapp, commandScreenshot # Importa los comandos desde otro archivo destinado únicamente a eso

class Assistant:
    def __init__(self, name:list, sensibilidad:int):
        self.name = name
        self.listener = sr.Recognizer()
        self.listener.energy_threshold = sensibilidad
        self.listener.dynamic_energy_threshold = False
        self.engine = pyttsx3.init() # TTS
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id) # Seleccion de voz (0 o 1)
        self.replace = {'á':'a', 'é':'e', 'í':'i',  'ó':'o', 'ú':'u'}

    def commands(self, rec:list): # Indica qué comando ejecutar
        # commandsKeys = []
        # print(commands)
        # for i in commands:
        #     commandsKeys.push("A")
        # print(commands)
        commandsKeys = ["reproduce", "patata", 'whatsapp', 'screenshot', 'captura', 'pantalla'] # Lista de comandos que detecta
        cmd = ""
        for a in commandsKeys:
                if a in rec: # Indica qué comando es según la posición en el array
                    pos = rec.index(a)+1
                    cmd = a
                    rec = rec[pos:]
                    break
        match cmd: # Busca el comando según el for anterior y la accion que debe hacer en dicho caso
            case 'reproduce':
                  self.reproduce(" ".join(rec))
                #   commandReproduce(Assistant, " ".join(rec))
            case 'whatsapp':
                self.whatsapp()
                # commandWhatsapp(Assistant)
            case 'captura':
                self.screenshot()
                # commandScreenshot(Assistant)
            case 'screenshot':
                self.screenshot()
                # commandScreenshot(Assistant)

    def reproduce(self, rec): # Comando reproducir
        print(f"Reproduciendo {rec}")
        self.talk(f"Reproduciendo {rec}")
        pywhatkit.playonyt(rec)
    
    def whatsapp(self, msg='', quien=''): # Comando whatsapp
        if msg == '' and quien == '':
            if pywhatkit.open_web(): self.talk("Whatsapp web abierto")

    def screenshot(self): # Comando captura
        pywhatkit.take_screenshot("MB_screenshot", show=False)
        self.talk('Captura de pantalla tomada con exito... quiere ver la captura?')
        rec = self.listen()
        if 'si' in rec: check_output(os.getcwd()+f'/MB_screenshot.png', shell=True)

    def talk(self, text): # TTS
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self): # Funcion de escucha
        try:
            with sr.Microphone() as source:
                print("escuchando...")
                self.listener.adjust_for_ambient_noise(source)
                pc = self.listener.listen(source)
                rec = self.listener.recognize_google(pc, language="es")
                rec = rec.lower()
                for a in rec: 
                    if a in self.replace: rec = rec.replace(a, self.replace[a])
        except:
            pass
        return rec

    def runAssistant(self, manual=False): # Inicia el asistente
        self.talk("Despertado y listo para ayudar.")
        while True:
            if not manual: rec = self.listen() # Si manual es true, espera texto, si no, detecta voz mediante la función listen
            else: 
                rec = input() # Indica que el comando es un input
                for a in rec: 
                    if a in self.replace: rec = rec.replace(a, self.replace[a])
            print("entendi: " + rec)
            for n in self.name:
                if n in rec:
                    rec = rec.replace(n, "") # Quita el nombre del asistente para analizar bien el comando
                    rec = rec.strip().split()
                    self.commands(rec) # Busca en los comandos qué debe ejecutar
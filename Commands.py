import pyttsx3, pywhatkit, os
from subprocess import check_output

def commandReproduce(self, rec): # Comando reproducir
    names = ["reproduce"]
    print(f"Reproduciendo {rec}")
    self.talk(f"Reproduciendo {rec}")
    pywhatkit.playonyt(rec)

def commandWhatsapp(self, msg='', quien=''): # Comando whatsapp
    names = ["whatsapp"]
    if msg == '' and quien == '':
        if pywhatkit.open_web(): self.talk("Whatsapp web abierto")

def commandScreenshot(self): # Comando captura
    names = ["screenshot", "captura"]
    pywhatkit.take_screenshot("MB_screenshot", show=False)
    self.talk('Captura de pantalla tomada con exito... quiere ver la captura?')
    rec = self.listen()
    if 'si' in rec: check_output(os.getcwd()+f'/MB_screenshot.png', shell=True)

def commandCalc(self):
    print(self)

commands = [commandReproduce, commandWhatsapp, commandScreenshot]

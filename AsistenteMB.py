import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import tempfile
import os
import pyttsx3
import re, string

sensibilidad = 1000
temp_file = tempfile.mkdtemp()
save_path = os.path.join(temp_file, 'temp.wav')
print(f'este es el path tmeporal: {save_path}')

chars = '[%s]+' % re.escape(string.punctuation)

listener = sr.Recognizer()
listener.energy_threshold = sensibilidad
listener.dynamic_energy_threshold = False

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 145) #velocidad de hablado Ns+ = -velocidad
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Di algo...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            data = io.BytesIO(audio.get_wav_data())
            audio_clip = AudioSegment.from_file(data)
            audio_clip.export(save_path, format='wav')
    except Exception as err:
        print(err)
    return save_path

def recognize_audio(save_path):
    audio_model = whisper.load_model('base')
    transcription = audio_model.transcribe(save_path, language = "spanish", fp16=False)
    return transcription['text']

def main():
    response = recognize_audio(listen())
    talk(response)
    print(re.sub(chars, '', response).lower().strip())
    if "bone" in re.sub(chars, '', response).lower().strip() or "bone" in re.sub(chars, '', response).lower().strip():
        accion = recognize_audio(listen())
        print(accion)
        if re.sub(chars, '', accion).lower().strip() == 'apagar': os.system("shutdown /s /t 1")

if __name__ == '__main__':
    main()
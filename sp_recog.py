from voice import class_voice
import speech_recognition as sr

class audio:
    def get_audio(self, text):
        recorder = sr.Recognizer()
        while True:
            try:
                with sr.Microphone() as source:
                    print("Say something...")
                    recorder.adjust_for_ambient_noise(source, duration=0.2)
                    audio = recorder.listen(source)
                    text = recorder.recognize_google(audio, language="es-Es")
                    text = text.lower()
                    print(f"You said: {text}")
                    return text
            except:
                recorder = sr.Recognizer()
                speak = "Te puedo ayudar en algo mas??"
                class_voice.fun_voice(speak)
                print(speak)
                continue





            

    

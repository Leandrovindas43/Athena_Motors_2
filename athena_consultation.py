from typing_extensions import Self
from cgitb import text
from sp_recog import audio
from voice import class_voice
import openai
openai.api_key = "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"
class class_consultation:
    def question():
        def enviar_prompt(prompt, engine="text-davinci-003", temp=0.5, max_tokens=1000, top_p=1, frequency_penalty=0, presence_penalty=0):
            respuesta = openai.Completion.create(
                                                    engine=engine,
                                                    prompt=prompt,
                                                    temperature=temp,
                                                    max_tokens=max_tokens,
                                                    top_p=top_p,
                                                    frequency_penalty=frequency_penalty,
                                                    presence_penalty=presence_penalty
                                                    )
            return respuesta['choices'][0]['text']
         
        speak = f"Cual seria su consulta?"
        class_voice.fun_voice(speak)
        entry = audio.get_audio(Self, text)
        respuesta = enviar_prompt(entry)
        class_voice.fun_voice(respuesta)
        


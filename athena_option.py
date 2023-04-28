from voice import class_voice
from athena_consultation import class_consultation
from athena_vin import class_vin
from main import class_question
from cgitb import text
from typing_extensions import Self
from cgitb import text
from sp_recog import audio
import openai
import pandas as pd
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
openai.api_key = "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"

def embed_text(path="texto.csv"):
    conocimiento_df = pd.read_csv(path)
    conocimiento_df['Embedding'] = conocimiento_df['text'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
    conocimiento_df.to_csv('embeddings/embeddings_option.csv')
    return conocimiento_df

def buscar(busqueda, datos, n_resultados=1):
    busqueda_embed = get_embedding(busqueda, engine="text-embedding-ada-002")
    datos["Similitud"] = datos['Embedding'].apply(lambda x: cosine_similarity(x, busqueda_embed))
    datos = datos.sort_values("Similitud", ascending=False)
    return datos.iloc[:n_resultados][["text", "Similitud", "Embedding", "code"]]

print("Buenas, mi nombre es Athena en que te puedo ayudar")
speak = f"Buenas, mi nombre es Atena en que te puedo ayudar"
class_voice.fun_voice(speak)

while True:
    #entry = input("tu: ")
    entry = audio.get_audio(Self, text)

    texto_emb = embed_text("primary_csv/option.csv")
    fun_2 = buscar(entry, texto_emb)
    fun_2 = pd.DataFrame(fun_2)
    code = fun_2["code"].to_list()
    text_str = fun_2["text"].to_list()
    print(text_str)
    for i in code:
        code = i
    for i in text_str:
        text_str = i

    if code == 1:
        print("Un momento")
        speak = f"Esta bien"
        class_voice.fun_voice(speak)
        obj = class_question
        obj.question()

    elif code == 2:
        print("re")
        speak = f"Un momento porfavor"
        class_voice.fun_voice(speak)
        obj = class_vin
        obj.vin()

    elif code == 3:
        print("re")
        speak = f"Un momento porfavor"
        class_voice.fun_voice(speak)
        obj = class_consultation
        obj.question()
        
        

    else:
        speak = "Desearia saber algo mas?"
        class_voice.fun_voice(text_str)
        print("Desea searia saber algo mas?")
        continue




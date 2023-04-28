from voice import class_voice
from sp_recog import audio
from typing_extensions import Self
from cgitb import text
from athena_parts import class_parts
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import pandas as pd
import pymysql
import openai

openai.api_key = "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"

connection = pymysql.connect(
    host='aws.connect.psdb.cloud',  # Si es remota "ip"
    user='3upo4vz7ot99y168410o',
    port=3306,
    passwd='pscale_pw_GPwjNJGmlvQGcjW2UkKMdgOGNNsiDUScYapoOAZWPXW',
    db='athena_motors',
    ssl      = {
    "ca": "/etc/ssl/cert.pem"
  }
)

class class_vin:
    
    def vin():
        def embed_text(path="texto.csv"):
            conocimiento_df = pd.read_csv(path)
            conocimiento_df['Embedding'] = conocimiento_df['text'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
            conocimiento_df.to_csv('embeddings/embeddings_confirm.csv')
            return conocimiento_df

        def buscar(busqueda, datos, n_resultados=1):
            busqueda_embed = get_embedding(busqueda, engine="text-embedding-ada-002")
            datos["Similitud"] = datos['Embedding'].apply(lambda x: cosine_similarity(x, busqueda_embed))
            datos = datos.sort_values("Similitud", ascending=False)
            return datos.iloc[:n_resultados][["text", "des", "code", "Similitud"]]

        while True:
            global plate_car
            print("Me podria decir el numero de placa de su vehiculo")
            speak = "Me podria decir el numero de placa de su vehiculo"
            class_voice.fun_voice(speak)

            #entry = input("tu: ")
            entry = audio.get_audio(Self, text)
            numebers = []
            for caracter in entry:
                if caracter.isdigit():
                    numebers.append(caracter)
            plate_car = int(''.join(map(str, numebers)))

            cursor = connection.cursor()
            cursor.execute(
                'SELECT Brand, Line, Year, PlateCar, Vim  FROM Cars WHERE PlateCar = "{}"'.format(plate_car))
            result = cursor.fetchall()

            if result == ():
                print(f"Me podria volver a repetir el numero de placa")
                speak = "Me podria volver a repetir el numero de placa"
                class_voice.fun_voice(speak)
                continue
            else:
                for i in result:
                    car_info = i
    
                print(f"Su auto es un {car_info[0]} modelo {car_info[1]} año {car_info[2]}")
                speak = f"Su auto es un {car_info[0]} modelo {car_info[1]} año {car_info[2]}"
                class_voice.fun_voice(speak)
    
                text_confirm = embed_text("primary_csv/confirm.csv")
                print(text_confirm)
                #entry = input("tu: ")
                entry = audio.get_audio(Self, text)
                fun = buscar(entry, text_confirm)
                fun = pd.DataFrame(fun)
                fun = fun["code"].to_list()
                for i in fun:
                    code = i
                print(code)
                print(type(code))
    
                if code == 0:
                    obj = class_parts
                    obj.parts(car_info[0], car_info[1],car_info[2], car_info[4])
                    
                elif code == 1:
                    continue
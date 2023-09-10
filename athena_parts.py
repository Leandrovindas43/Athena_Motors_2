import openai
import pymysql
import re
import pandas as pd
from typing_extensions import Self
from cgitb import text
from sp_recog import audio
from athena_register import class_register
from voice import class_voice
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
openai.api_key = "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"

connection = pymysql.connect(
    host='aws.connect.psdb.cloud',  # Si es remota "ip"
    user='xbmc1wn15bbl5wdezy8h',
    port=3306,
    passwd='pscale_pw_Srzi7GvBZ3Cppbth9zkUW8RKZgl321Gd1kV99DSCTSx',
    db='athena_motors',
    ssl      = {
    "ca": "/etc/ssl/cert.pem"
  }
)
cursor = connection.cursor()

class class_parts:
    def parts(brand, line, year, vin):
        def embed_text():
            conocimiento_df = pd.DataFrame(cursor.fetchall(), columns = ["Vin", "PartNumber", "Brand", "Price", "ProductName"])
            conocimiento_df['Embedding'] = conocimiento_df['ProductName'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
            conocimiento_df.to_csv('embeddings/embeddings_parts.csv')
            print(conocimiento_df)
            return conocimiento_df

        def buscar(busqueda, datos, n_resultados=1):
            busqueda_embed = get_embedding(busqueda, engine="text-embedding-ada-002")
            datos["Similitud"] = datos['Embedding'].apply(lambda x: cosine_similarity(x, busqueda_embed))
            datos = datos.sort_values("Similitud", ascending=False)
            return datos.iloc[:n_resultados][["ProductName", "Vin", "PartNumber", "Similitud", "Embedding"]]

        cursor.execute('''
                  SELECT
                  *
                  FROM Engine WHERE Vin = "{}"
                  '''.format(vin))
        
        print (f"Podria decirme el repuesto que solicita")
        speak = f"Podria decirme el repuesto que solicita"
        class_voice.fun_voice(speak)

        while True:
            entry = audio.get_audio(Self, text)
            #entry = input("tu: ")

            fun_1 = embed_text()
            fun_2 = buscar(entry, fun_1)
            print(fun_2)
            fun_2 = pd.DataFrame(fun_2)
            simi_list = fun_2["Similitud"].to_list()
            part_list = fun_2["PartNumber"].to_list()

            for i in simi_list:
                simi_var = i

            for i in part_list:
                part_var = i

            if simi_var > 0.79:
                cursor.execute('''
                      SELECT
                      *
                      FROM Engine WHERE PartNumber = "{}"
                      '''.format(part_var))
                result = cursor.fetchall()
                print(result)
                for i in result:
                    part_info = i
                print(part_info)
                obj = class_register
                obj.register(brand, line, year, vin, part_info[1], part_info[2], part_info[3], part_info[4])
            else:
                print("No tenemos ese repuesto, desea otro?")
                speak = "No tenemos ese repuesto, desea otro?"
                class_voice.fun_voice(speak)
                continue
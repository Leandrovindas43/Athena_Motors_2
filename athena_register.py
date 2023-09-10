from voice import class_voice
from sp_recog import audio
from typing_extensions import Self
from cgitb import text
from athena_mail import class_mail
import pymysql
import re

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

connection_2 = pymysql.connect(
        host='localhost',  # Si es remota "ip"
        user='root',
        port=3306,
        passwd='Leandro01',
        db='motors'
)

class class_register:
    def register(brand, line, year, vin, part_number, brand_part, price, product_Name):
        print (f"Me podria facilitar su numero de identificacion")
        speak = f"Me podria facilitar su numero de identificacion"
        class_voice.fun_voice(speak)

        #entry = input("tu: ")
        entry = audio.get_audio(Self, text)
        numebers = []
        for caracter in entry:
            if caracter.isdigit():
                numebers.append(caracter)
        id = int(''.join(map(str, numebers)))

        cursor = connection.cursor()
        cursor.execute( 'SELECT *  FROM Person WHERE PersonID = "{}"'.format(id))
        result = cursor.fetchall()
        print(result)

        if result == ():
            print (f"Usted no esta registrado, porfavor me podria facilitar su correo electronico")
            speak = f"Usted no esta registrado, porfavor me podria facilitar su correo electronico"
            class_voice.fun_voice(speak)
            
            #entry = input("tu: ")
            entry = audio.get_audio(Self, text)
            match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', entry)
            mail = match.group(0)
            print(mail)
            
            #base de datos de las cedulas
            cursor_2 = connection_2.cursor()
            cursor_2.execute('SELECT * FROM ID WHERE ID = "{}"'.format(id))
            user = cursor_2.fetchone()
            print(user)
            last_name = user[6] + user[7]
            print(last_name)

           #insertar en la base de datos de los Person de la nube 
            sql = '''
                INSERT INTO Person (PersonID, LastName, Name, Adress, City, Mail) 
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}')
                '''.format(user[0], last_name , user[5], "none", "none", mail)
            cursor.execute(sql)
            connection.commit()
            speak = "Su compra se a realizado con exito"
            class_voice.fun_voice(speak)
            obj = class_mail
            obj.mail(id, brand, line, year, vin, part_number, brand_part, price, product_Name)
            
        else:
            speak = "Su compra se a realizado con exito"
            class_voice.fun_voice(speak)
            obj = class_mail
            obj.mail(id, brand, line, year, vin, part_number, brand_part, price, product_Name)
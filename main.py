import os
import pymongo
import time

url = os.environ['URL']
cli = pymongo.MongoClient(url)
db = cli["texpeed"]
while (True):
    os.system("clear")
    print("Bienvenido/a a Texpeed\nSelecciona una opcion\n\n1: Login\n2: Crear cuenta")
    sel = input()
    os.system("clear")
    login = input("Usuario: ")
    passw = input("Contraseña: ")
    if (sel == "1" or sel == "login"):
        users = db.list_collection_names()
        pas = 0
        if login in users:
            col = db[login]
            for i in col.find():
                try:
                    if i["password"] == passw:
                        pas = 1
                        break
                except IndexError:
                    pass
            if pas == 1:
                break
            else:
                print("La contraseña no es correcta")
                time.sleep(1)
                continue    
        else:
            print("No se ha encontrado tu usuario")
            time.sleep(1)
            continue
    elif (sel == "2" or sel == "crear cuenta"):
        users = db.list_collection_names()
        if login in users:
            print("Este usuario ya tiene una cuenta")
            time.sleep(1)
            continue
        else:
            col = db[login]
            col.insert_one({"password": passw})

print("Lo conseguiste")
exit()
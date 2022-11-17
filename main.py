import os
import pymongo
import time

url = os.environ['url']
cli = pymongo.MongoClient(url)
db = cli["texpeed"]
col = db["users"]
while (True):
    os.system("clear")
    print("Bienvenido/a a Texpeed\nSelecciona una opcion\n\n1: Login\n2: Crear cuenta")
    sel = input()
    os.system("clear")
    login = input("Login: ")
    passw = input("Contraseña: ")
    if (sel == "1" or sel == "login"):
        try:
            for x in col.find():
                if x[login]:
                    if x[login] != passw:
                        raise IndexError
                    else:
                        break
                else:
                    raise IndexError
        except Exception:
            print("No se ha encontrado tu login o la contraseña esta mal")
            continue
        break
    elif (sel == "2" or sel == "crear cuenta"):
        for x in col.find():
            if x[login]:
                print("Ya hay un usuario con este login\n")
                time.sleep(1)
                break
        col.insert_one({login: passw})

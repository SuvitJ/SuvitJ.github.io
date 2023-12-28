from deta import Deta

DETA_KEY = ""

deta = Deta(DETA_KEY)

db = deta.Base("user_db")

def insert_user(username, name, password):
    return db.put({"key": username, "name": name, "password": password})

insert_user("pparker","Peter Parker","abc123")

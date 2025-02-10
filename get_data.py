import sqlite3
import json

def get_suspects():
    conn = sqlite3.connect("escape_game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM suspects")
    suspects = cursor.fetchall()
    conn.close()
    return json.dumps([{"id": s[0], "nom": s[1], "role": s[2], "description": s[3]} for s in suspects], indent=4)

def get_objets():
    conn = sqlite3.connect("escape_game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM objets")
    objets = cursor.fetchall()
    conn.close()
    return json.dumps([{"id": o[0], "nom": o[1], "description": o[2], "indice_cache": o[3]} for o in objets], indent=4)

def get_enigmes():
    conn = sqlite3.connect("escape_game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM enigmes")
    enigmes = cursor.fetchall()
    conn.close()
    return json.dumps([{"id": e[0], "question": e[1], "reponse": e[2]} for e in enigmes], indent=4)

# Sauvegarder les données dans des fichiers JSON
with open("suspects.json", "w", encoding="utf-8") as f:
    f.write(get_suspects())

with open("objets.json", "w", encoding="utf-8") as f:
    f.write(get_objets())

with open("enigmes.json", "w", encoding="utf-8") as f:
    f.write(get_enigmes())

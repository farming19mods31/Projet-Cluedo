import sqlite3

def creer_db():
    conn = sqlite3.connect("escape_game.db")
    cursor = conn.cursor()

    # Table des suspects
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suspects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            role TEXT,
            description TEXT
        )
    """)

    # Table des objets trouvés
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS objets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            description TEXT,
            indice_cache TEXT
        )
    """)

    # Table des énigmes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enigmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            reponse TEXT
        )
    """)

    conn.commit()
    conn.close()

creer_db()

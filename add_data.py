import sqlite3

def ajouter_donnees():
    conn = sqlite3.connect("escape_game.db")
    cursor = conn.cursor()

    # Ajouter des suspects
    suspects = [
        ("Antoine Morel", "Conservateur", "Expert en art, suspecté d’avoir préparé une copie."),
        ("Sophie Laurent", "Restauratrice", "A des compétences pour faire des reproductions."),
        ("Léo Fontaine", "Gardien de nuit", "A désactivé les caméras."),
        ("Maxime Dubois", "Faux touriste", "A été vu prendre des notes sur la Joconde.")
    ]

    cursor.executemany("INSERT INTO suspects (nom, role, description) VALUES (?, ?, ?)", suspects)

    # Ajouter des objets trouvés
    objets = [
        ("Double des clés", "Clés du conservateur retrouvées sur la scène du crime.", "Elles ouvrent une porte secrète."),
        ("Gants tachés de peinture", "Gants retrouvés dans l'atelier de Sophie Laurent.", "La peinture est fluorescente sous UV."),
        ("Chariot de transport", "Un chariot utilisé pour déplacer des œuvres.", "Il y a des traces de poussière récentes."),
        ("Fausse Joconde", "Une copie presque parfaite du tableau.", "Mais un détail cloche : la signature est absente.")
    ]

    cursor.executemany("INSERT INTO objets (nom, description, indice_cache) VALUES (?, ?, ?)", objets)

    # Ajouter des énigmes
    enigmes = [
        ("Quel est le code pour ouvrir le passage secret ?", "1911"),
        ("Quel suspect a un alibi vérifiable ?", "Sophie Laurent"),
        ("Quel objet a été utilisé pour dissimuler la Joconde ?", "Fausse Joconde")
    ]

    cursor.executemany("INSERT INTO enigmes (question, reponse) VALUES (?, ?)", enigmes)

    conn.commit()
    conn.close()

ajouter_donnees()

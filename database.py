import os
import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS commandes (
            id SERIAL PRIMARY KEY,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL,
            telephone TEXT NOT NULL,
            adresse TEXT NOT NULL,
            produit TEXT NOT NULL,
            prix INTEGER NOT NULL,
            remise INTEGER NOT NULL,
            total INTEGER NOT NULL,
            rating INTEGER
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

def ajouter_commande(nom, prenom, email, telephone, adresse, produit, prix, remise, total, rating):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO commandes
        (nom, prenom, email, telephone, adresse, produit, prix, remise, total, rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (nom, prenom, email, telephone, adresse, produit, prix, remise, total, rating))

    conn.commit()
    cur.close()
    conn.close()
